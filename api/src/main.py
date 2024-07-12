from fastapi import FastAPI

from src.routers import task, auth

app = FastAPI()

app.include_router(task.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
