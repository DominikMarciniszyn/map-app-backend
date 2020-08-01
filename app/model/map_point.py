from .base_model import BaseModel
from peewee import CharField, NumberField, UUIDField


class MapPoint(BaseModel):
    name = CharField(unique=True)
    latitude = NumberField()
    longitude = NumberField()
    external_id = UUIDField()
