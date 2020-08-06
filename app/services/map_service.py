from ..schemas.map import Map as MapSchema
from ..model.map import Map
from playhouse.shortcuts import model_to_dict


OBJECT_EXISTS = (
    'Map object you would like to create already exists in the database'
)
OBJECT_DOES_NOT_EXIST = (
    'This object does not exist in the database'
)


class MapService:
    def create_map(self, map: MapSchema):
        map_object = Map(
            name=map.name,
            latitude=map.latitude,
            longitude=map.longitude,
            zoom_level=map.zoom
        )

        result = self.get_map_by_name(map_object.name)

        if result:
            return {'Result': OBJECT_EXISTS}
        else:
            map_object.save()
            return model_to_dict(map_object)

    def get_maps(self):
        maps = list()
        query = Map.select().objects()

        for item in query:
            maps.append(model_to_dict(item))

        return maps

    def get_map_by_name(self, mapName: str):
        result = Map.get(Map.name == mapName)
        return model_to_dict(result)

    def get_map_by_id(self, mapID: int):
        try:
            result = Map.get_by_id(mapID)
            return model_to_dict(result)
        except Exception:
            return {'Result': OBJECT_DOES_NOT_EXIST}

    def update_map(self, map: MapSchema):
        db_map = Map.update(map)
        db_map.save()
        return db_map

    def delete_map_by_name(self, mapID: int):
        result = Map.delete().where(Map.id == mapID)
        return result
