from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db
from src.schemas.task import TaskCreateResponse, TaskCreateRequest, TaskIndexResponse
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

@router.get("/tasks", response_model=TaskIndexResponse, tags=["tasks"])
async def get_tasks(db: Session = Depends(get_db)):
    # task_repository = TaskRepository(db)
    # tasks = task_repository.get_all()

    # return tasks
    return {
        "tasks": [
                    {"id": 1, "title": "クリーニングに取りに行く", "description": "〇〇クリーニングに取りに行く", "finished_at": None, "created_at": "2024-09-01T00:00:00"},
                    {"id": 2, "title": "ゴミ捨て", "description": "〇〇ゴミ捨て", "finished_at": "2024-10-01T00:00:00", "created_at": "2024-09-01T00:00:00"},
                ]
    }