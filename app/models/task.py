from typing import datetime, date
from pydantic import BaseModel


class tasks(BaseModel):
    title: str
    done: bool
    deadline: date
    created_at: datetime
    updated_at: datetime
