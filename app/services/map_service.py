from ..schemas.map import Map as MapSchema
from ..model.map import Map


class MapService:
    def create_map(self, map: MapSchema):
        db_map = Map(
            name=map.name,
            latitude=map.latitude,
            longitude=map.longitude,
            zoom_level=map.zoom
        )

        result = self.get_map_by_name(db_map.name)

        if result:
            return {'Result': 'Given object already exists in the database'}
        else:
            db_map.save()
            return db_map

    def get_maps(self):
        query = Map.select().objects()

        for item in query:
            print(item)

        return query

    def get_map_by_name(self, mapName: str):
        pass

    def get_map_by_id(self, mapID: int):
        result = Map.get_by_id(mapID)
        return result

    def update_map(self, map: MapSchema):
        db_map = Map.update(map)
        db_map.save()
        return db_map

    def delete_map_by_name(self, mapID: int):
        result = Map.delete().where(Map.id == mapID)
        return result
