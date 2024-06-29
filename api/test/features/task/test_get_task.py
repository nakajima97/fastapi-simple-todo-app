import pytest
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_get_task_empty(async_client: AsyncSession):
    response = await async_client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == {"tasks": []}
