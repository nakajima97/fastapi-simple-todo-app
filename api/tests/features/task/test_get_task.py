import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_task_empty(async_client: AsyncSession):
    """
    データが存在しない際に正しく空のリストを返すことを確認するテスト
    """
    response = await async_client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == {"tasks": []}


@pytest.mark.asyncio
async def test_get_tasks(async_client: AsyncClient, dummy_tasks):
    """
    データが存在する際に正しくデータを取得できることを確認するテスト
    """
    response = await async_client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data["tasks"]) == 2

    # enumerateを使ってインデックスとデータを同時に取得
    for i, task_data in enumerate(data["tasks"]):
        assert task_data["title"] == dummy_tasks[i].title
        assert task_data["description"] == dummy_tasks[i].description
