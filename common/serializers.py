from pydantic import BaseModel


class ErrorSerializer(BaseModel):
    error: str
    detail: str
