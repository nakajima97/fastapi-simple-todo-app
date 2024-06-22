from pydantic import BaseModel, Field
from datetime import datetime

class TaskCreateResponse(BaseModel):
    title: str = Field(..., example="クリーニングに取りに行く")
    description: str | None = Field(None, example="〇〇クリーニングに取りに行く")