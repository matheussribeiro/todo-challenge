from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class BaseModel(Model):
    id: str = UnicodeAttribute(hash_key=True)
