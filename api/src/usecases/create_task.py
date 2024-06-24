class CreateTask:
    def __init__(self, task_repo):
        self.task_repo = task_repo

    def exec(self, task):
        return self.task_repo.create(task)
