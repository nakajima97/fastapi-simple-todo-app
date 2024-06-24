from pydantic import BaseModel, Field

class TaskCreateResponse(BaseModel):
    result: str = Field(..., example="Task created successfully")

class TaskCreateRequest(BaseModel):
    title: str = Field(..., example="クリーニングに取りに行く")
    description: str | None = Field(None, example="〇〇クリーニングに取りに行く")