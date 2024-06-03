from typing import datetime
from pydantic import BaseModel


class users(BaseModel):
    u_name: str
    password: str
    email: str
    created_at: datetime
    updated_at: datetime
