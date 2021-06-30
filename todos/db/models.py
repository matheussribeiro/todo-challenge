from db.services import DBService
from pynamodb.attributes import UnicodeAttribute
from todos.serializers import TodoSerializer
from db.models import BaseModel


class TodoModel(BaseModel):
    title: str = UnicodeAttribute()

    class Meta:
        table_name = DBService.table_name('todo')
        host = DBService.host()

    @property
    def serialized(self):
        return TodoSerializer.from_orm(self)
