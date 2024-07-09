import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.task import Task
from src.repositories.task_repository import TaskRepository

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest.mark.asyncio
async def test_create_task(async_session: AsyncSession):
    task = Task(title="Test Task", description="Test Description")
    task_repository = TaskRepository(async_session)

    # createメソッドを実行
    created_task = await task_repository.create(task)

    # アサーション
    assert created_task.id is not None  # IDが自動採番されていることを確認
    assert created_task.title == "Test Task"
    assert created_task.description == "Test Description"

    # データベースに保存されているか確認
    fetched_task = await async_session.get(Task, created_task.id)
    assert fetched_task is not None
    assert fetched_task.title == "Test Task"
    assert fetched_task.description == "Test Description"
