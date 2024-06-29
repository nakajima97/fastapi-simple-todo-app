class CreateTask:
    def __init__(self, task_repo):
        self.task_repo = task_repo

    async def exec(self, task):
        return await self.task_repo.create(task)
