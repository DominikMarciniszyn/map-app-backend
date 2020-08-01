from .base_model import BaseModel
from peewee import CharField, NumberField


class Map(BaseModel):
    name = CharField(unique=True)
    latitude = NumberField()
    longitude = NumberField()
    zoom_level = NumberField()
