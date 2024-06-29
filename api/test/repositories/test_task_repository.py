import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from migrations.models import Base
from src.models.task import Task
from src.repositories.task_repository import TaskRepository

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

async_engine = create_async_engine(ASYNC_DB_URL, echo=False)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)


@pytest_asyncio.fixture
async def async_client():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session():
    async with async_session() as session:
        yield session

@pytest.mark.asyncio
async def test_create_task(async_client):
    async with async_session() as session:
        task = Task(title="Test Task", description="Test Description")
        task_repository = TaskRepository(session)

        # createメソッドを実行
        created_task = await task_repository.create(task)

        # アサーション
        assert created_task.id is not None  # IDが自動採番されていることを確認
        assert created_task.title == "Test Task"
        assert created_task.description == "Test Description"

        # データベースに保存されているか確認
        fetched_task = await session.get(Task, created_task.id)
        assert fetched_task is not None
        assert fetched_task.title == "Test Task"
        assert fetched_task.description == "Test Description"