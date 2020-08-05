from .base_model import BaseModel
from peewee import (
    CharField,
    FloatField,
    UUIDField,
    ForeignKeyField
)
from .map import Map


class MapPoint(BaseModel):
    name = CharField(unique=True)
    latitude = FloatField()
    longitude = FloatField()
    external_id = UUIDField()
    map_id = ForeignKeyField(Map, backref='map_id')

    class Meta:
        db_table = 'map_point'
