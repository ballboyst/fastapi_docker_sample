from Pydantic import BaseModel
from datetime import date


class Get_tasks(BaseModel):
    id: int
    task_name: str
    done: bool
    deadline: date
