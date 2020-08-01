from .base_model import BaseModel
from peewee import CharField, NumberField, AutoField


class Map(BaseModel):
    map_id = AutoField()
    name = CharField(unique=True)
    latitude = NumberField()
    longitude = NumberField()
    zoom_level = NumberField()
