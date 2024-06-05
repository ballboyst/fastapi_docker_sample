from Pydantic import BaseModel
from datetime import date


class base_tasks(BaseModel):
    title: str
    deadline: date

class get_tasks(base_tasks):
    id: int
    done: bool

class create_tasks(base_tasks):

class update_tasks(base_tasks):
    done : bool

class delete_tasks(BaseModel):
    id: int