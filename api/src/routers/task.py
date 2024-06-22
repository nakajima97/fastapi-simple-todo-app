from fastapi import APIRouter

from src.schemas.task import TaskCreateResponse

router = APIRouter()

@router.post("/tasks")
async def create_task(task_body: TaskCreateResponse):
    return {"message": "Task created successfully"}