from .base_model import BaseModel
from peewee import (
    CharField,
    FloatField,
    IntegerField,
    AutoField
)


class Map(BaseModel):
    map_id = AutoField()
    name = CharField(unique=True)
    latitude = FloatField()
    longitude = FloatField()
    zoom_level = IntegerField()
