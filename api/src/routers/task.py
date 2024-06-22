from fastapi import APIRouter

from src.schemas.task import TaskCreateResponse, TaskCreateRequest

router = APIRouter()

@router.post("/tasks", response_model=TaskCreateResponse, tags=["tasks"])
async def create_task(task_body: TaskCreateRequest):
    return {"result": "Task created successfully"}