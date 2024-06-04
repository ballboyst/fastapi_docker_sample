from Pydantic import BaseModel
from datetime import date


class Get_tasks(BaseModel):
    id: int
    title: str
    done: bool
    deadline: date
