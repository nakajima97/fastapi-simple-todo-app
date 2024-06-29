from pydantic import BaseModel, Field


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
