from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db
from src.schemas.task import TaskCreateResponse, TaskCreateRequest, TaskIndexResponse
from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.usecases.create_task import CreateTask
from src.usecases.fetch_all_tasks import FetchAllTasks
from src.usecases.finish_task import FinishTask

router = APIRouter()


@router.post("/tasks", response_model=TaskCreateResponse, tags=["tasks"])
async def create_task(task_body: TaskCreateRequest, db: Session = Depends(get_db)):
    '''
    タスクを作成する
    '''
    task = Task(**task_body.model_dump())

    task_repository = TaskRepository(db)
    await CreateTask(task_repository).exec(task)

    return {"result": "Task created successfully"}


@router.get("/tasks", response_model=TaskIndexResponse, tags=["tasks"])
async def get_tasks(db: Session = Depends(get_db)):
    '''
    タスク一覧を取得する
    '''
    task_repository = TaskRepository(db)

    fetch_all_tasks = FetchAllTasks(task_repository)
    tasks = await fetch_all_tasks.exec()

    return {"tasks": tasks}

@router.put("/tasks/{id}/finish", response_model=TaskCreateResponse, tags=["tasks"])
async def finish_task(id: int, db: Session = Depends(get_db)):
    '''
    タスクを完了する
    '''
    task_repository = TaskRepository(db)

    finish_task = FinishTask(task_repository)
    await finish_task.exec(id)

    return {"result": "Task finished successfully"}