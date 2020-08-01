from .base_model import BaseModel
from peewee import (
    CharField,
    NumberField,
    UUIDField,
    ForeignKeyField
)
from map import Map


class MapPoint(BaseModel):
    name = CharField(unique=True)
    latitude = NumberField()
    longitude = NumberField()
    external_id = UUIDField()
    map = ForeignKeyField(Map, backref='map_id')
