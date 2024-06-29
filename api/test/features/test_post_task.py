import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from alembic import command
from alembic.config import Config

from src.main import app  # FastAPI アプリケーションをインポート
from src.db import get_db
from src.models.task import Task  # Taskモデルをインポート
from src.repositories.task_repository import TaskRepository
from migrations.models import Base # alembicで設定しているBaseをインポート

# テスト用DB接続情報
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="session")
def engine():
    """テスト実行全体で共有されるエンジン"""
    engine = create_engine(TEST_DATABASE_URL)
    yield engine
    engine.dispose()

@pytest.fixture(scope="session")
def tables(engine):
    """テスト開始時にテーブルを作成し、終了時に削除"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def session(engine, tables) -> Session:
    """各テスト関数で利用するセッション"""
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker()(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="session")
def alembic_config():
    """alembic設定をオーバーライド"""
    config = Config("alembic.ini")  # alembic.ini ファイルのパスを指定
    config.set_main_option("sqlalchemy.url", TEST_DATABASE_URL)
    return config

@pytest.fixture(scope="session", autouse=True)
def apply_migrations(alembic_config, engine):
    """テスト開始前にマイグレーションを実行"""
    command.upgrade(alembic_config, "head")

@pytest.fixture
def client(session):
    """FastAPI アプリケーションのテストクライアント"""

    # 依存関係をオーバーライドしてテスト用のセッションを提供
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db  # get_db 関数をオーバーライド
    with TestClient(app) as client:
        yield client
    app.dependency_overrides = {}  # オーバーライドをリセット


def test_create_task(client: TestClient, session: Session):
    """TaskRepository.create()のテスト"""
    
    # リクエストボディ
    task_data = {"title": "Test Task", "description": "Test Description"}

    # リクエストを送信
    response = client.post("/tasks", json=task_data)

    # レスポンスを確認
    assert response.status_code == 200
    assert response.json() == {"result": "Task created successfully"}

    # データベースの内容を確認
    task = session.query(Task).filter_by(title="Test Task").first()
    assert task is not None
    assert task.description == "Test Description"