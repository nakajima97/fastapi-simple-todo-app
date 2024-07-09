import pytest
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_finish_task(async_client: AsyncSession, dummy_tasks):
    '''
    タスクを完了したときのテスト
    '''
    response = await async_client.put("/tasks/1/finish")
    assert response.status_code == 200
    assert response.json() == {"result": "Task finished successfully"}

@pytest.mark.asyncio
async def test_finish_task_when_task_not_found(async_client: AsyncSession):
    '''
    タスクが見つからないときのテスト
    '''
    response = await async_client.put("/tasks/1/finish")
    assert response.status_code == 200
    assert response.json() == {"result": "Task not found"}