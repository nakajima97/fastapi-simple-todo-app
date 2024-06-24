from sqlalchemy.orm import Session

from src.models.task import Task


class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task
