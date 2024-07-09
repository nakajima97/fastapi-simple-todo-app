import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from migrations.models import Base
from src.main import app
from src.db import get_db
from src.models.task import Task

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def async_session():
    async_engine = create_async_engine(ASYNC_DB_URL, echo=False)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        yield session


@pytest_asyncio.fixture
async def async_client(async_session: AsyncSession):  # async_sessionフィクスチャを使う
    async def get_test_db():
        yield async_session  # async_sessionをそのまま返す

    app.dependency_overrides[get_db] = get_test_db

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client

@pytest_asyncio.fixture
async def dummy_tasks(async_session: AsyncSession):
    """
    ダミータスクデータを作成するフィクスチャ
    """
    task1 = Task(title="Task 1", description="Description 1")
    task2 = Task(title="Task 2", description="Description 2")
    async_session.add_all([task1, task2])
    await async_session.commit()

    # テスト関数で利用できるようにタスクのリストを返す
    # yieldをfixtureで使うのは一つの慣習
    # 今回は不要だがクリーンアップ処理をテストでは行うことが多いのでこういった慣習になっている
    yield [task1, task2]