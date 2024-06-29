import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.models.task import Task  # Taskモデルをインポート
from src.repositories.task_repository import TaskRepository  # TaskRepositoryをインポート

@pytest.fixture
def session():
    """テスト用のインメモリDBとセッション"""
    engine = create_engine("sqlite:///:memory:")
    Task.__table__.create(bind=engine)  # テーブルを作成
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def test_create_task(session: Session):
    """TaskRepository.create()のテスト"""
    repository = TaskRepository(session)  # テスト用のセッションを使用

    task = Task(title="Test Task", description="Test Description")  # テストデータ

    # createメソッドを実行
    created_task = repository.create(task)

    # アサーション
    assert created_task.id is not None  # IDが自動採番されていることを確認
    assert created_task.title == "Test Task"
    assert created_task.description == "Test Description"

    # データベースに保存されているか確認
    fetched_task = session.query(Task).filter_by(id=created_task.id).first()
    assert fetched_task is not None
    assert fetched_task.title == "Test Task"
    assert fetched_task.description == "Test Description"