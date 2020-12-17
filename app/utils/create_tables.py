from ..model.map import Map
from ..model.map_point import MapPoint


def create_tables():
    Map.create_table()
    MapPoint.create_table()
