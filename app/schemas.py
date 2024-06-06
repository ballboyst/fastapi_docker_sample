from pydantic import BaseModel
from datetime import date


class TaskBase(BaseModel):
    title: str

class TaskGet(TaskBase):
    id: int
    done: bool
    deadline: date

class TaskCreate(TaskBase):
    deadline: date

class UpdateTask(TaskBase):
    done : bool
    deadline: date


class DeleteTask(BaseModel):
    id: int
