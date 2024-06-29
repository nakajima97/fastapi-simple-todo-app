from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class Task(BaseModel):
    id: int
    title: str
    description: str | None
    finished_at: datetime | None
    created_at: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "1",
                "title": "クリーニングに取りに行く",
                "description": "〇〇クリーニングに取りに行く",
                "finished_at": "2024-10-01T00:00:00",
                "created_at": "2024-09-01T00:00:00",
            }
        }
    }


class TaskIndexResponse(BaseModel):
    tasks: List[Task]

    model_config = {
        "json_schema_extra": {
            "example": {
                "tasks": [
                    {
                        "id": 1,
                        "title": "クリーニングに取りに行く",
                        "description": "〇〇クリーニングに取りに行く",
                        "finished_at": "",
                        "created_at": "2024-09-01T00:00:00",
                    },
                    {
                        "id": 2,
                        "title": "ゴミ捨て",
                        "description": "〇〇ゴミ捨て",
                        "finished_at": "2024-10-01T00:00:00",
                        "created_at": "2024-09-01T00:00:00",
                    },
                ]
            }
        }
    }


class TaskCreateResponse(BaseModel):
    result: str = Field(...)

    model_config = {
        "json_schema_extra": {"example": {"result": "Task created successfully"}}
    }


class TaskCreateRequest(BaseModel):
    title: str = Field(...)
    description: str | None = Field(None)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "クリーニングに取りに行く",
                "description": "〇〇クリーニングに取りに行く",
            }
        }
    }
