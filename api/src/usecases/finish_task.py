from src.repositories.task_repository import TaskRepository

class FinishTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def exec(self, task_id: int) -> None:
        await self.task_repository.finish_task(task_id)