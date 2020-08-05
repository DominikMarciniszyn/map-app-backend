from peewee import (
    CharField,
    FloatField,
    IntegerField,
    AutoField
)
from .base_model import BaseModel


class Map(BaseModel):
    id = AutoField()
    name = CharField(unique=True)
    latitude = FloatField()
    longitude = FloatField()
    zoom_level = IntegerField()

    class Meta:
        db_table = 'map'
