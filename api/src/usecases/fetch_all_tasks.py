from src.repositories.task_repository import TaskRepository


class FetchAllTasks:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def exec(self):
        return await self.task_repository.fetch_all()
