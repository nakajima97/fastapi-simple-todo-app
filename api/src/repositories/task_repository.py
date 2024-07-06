from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, update
from datetime import datetime

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

    async def finish(self, task_id: int):
        '''
        タスクを完了する
        '''
        # 検索対象のタスクを取得する
        result = await self.session.execute(select(Task).filter(Task.id == task_id))
        task = result.scalars().first()

        # タスクが存在しない場合はエラーを返す
        if task is None:
            raise ValueError("Task not found")

        # タスクが完了済みだったら何もせずに終了する
        if task.finished_at is not None:
            return task

        # 値を更新する
        task.finished_at = datetime.now()

        # 更新をコミットする
        await self.session.commit()
        await self.session.refresh(task)

        # 更新後のタスクを返す
        return task