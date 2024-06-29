from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from src.models.task import Task


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, task: Task):
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def fetch_all(self):
        result = await self.session.execute(select(Task))
        return result.scalars().all()