from fastapi import APIRouter

router = APIRouter()

@router.post("/tasks")
async def create_task():
    return {"message": "Task created successfully"}