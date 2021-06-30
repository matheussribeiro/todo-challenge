from pydantic import BaseModel


class TodoSerializer(BaseModel):
    id: str
    title: str

    class Config:
        orm_mode = True


class TodoCreateSerializer(BaseModel):
    title: str
