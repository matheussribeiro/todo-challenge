from .enums import Status
from pydantic import BaseModel
from datetime import datetime



class TodoSerializer(BaseModel):
    id: str
    title: str
    description: str
    status: Status
    due_date: datetime
    responsible: str

    class Config:
        orm_mode = True


class TodoCreateSerializer(BaseModel):
    title: str
    description: str
    status: Status
    due_date: datetime
    responsible: str

