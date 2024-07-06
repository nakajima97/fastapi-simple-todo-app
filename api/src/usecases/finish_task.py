from src.repositories.task_repository import TaskRepository


class FinishTask:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def exec(self, task_id: int) -> None:
        try:
            await self.task_repository.finish(task_id)
        except ValueError as e:
            raise e
