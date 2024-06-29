import pytest
from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from tests.features.conftest import ASYNC_DB_URL, async_session  # async_sessionをインポート

@pytest.mark.asyncio
async def test_get_task_empty(async_client: AsyncSession):
    response = await async_client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == {"tasks": []}

# @pytest.mark.asyncio
# async def test_get_tasks(async_client: AsyncClient, async_session: AsyncSession):
#     # ダミーデータを入れる

#     response = await async_client.get("/tasks")

#     assert response.status_code == 200
#     assert response.json() == {
#         "tasks": [
#             {
#                 "id": 1,
#                 "title": "Test Task",
#                 "description": "Test Description",
#             }
#         ]
#    }