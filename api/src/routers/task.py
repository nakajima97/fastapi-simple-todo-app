from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db
from src.schemas.task import TaskCreateResponse, TaskCreateRequest
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.usecases.create_task import CreateTask

router = APIRouter()


@router.post("/tasks", response_model=TaskCreateResponse, tags=["tasks"])
async def create_task(task_body: TaskCreateRequest, db: Session = Depends(get_db)):
    task = Task(**task_body.model_dump())

    task_repository = TaskRepository(db)
    await CreateTask(task_repository).exec(task)

    return {"result": "Task created successfully"}
