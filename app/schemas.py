from pydantic import BaseModel
from datetime import date


class TaskCreate(BaseModel):
    title: str
    deadline: date


class UpdateTask(TaskCreate):
    id: int
    done: bool


class DeleteTask(BaseModel):
    id: int
