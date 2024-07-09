import pytest
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_finish_task(async_client: AsyncSession, dummy_tasks):
    response = await async_client.put("/tasks/1/finish")
    assert response.status_code == 200
    assert response.json() == {"result": "Task finished successfully"}