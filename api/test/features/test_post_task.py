import pytest
from sqlalchemy.ext.asyncio import AsyncSession



@pytest.mark.asyncio
async def test_post_task(async_client: AsyncSession):
    response = await async_client.post(
        "/tasks", json={"title": "Test Task", "description": "Test Description"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": "Task created successfully"}
