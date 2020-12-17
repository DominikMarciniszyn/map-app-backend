from fastapi import APIRouter
from ..schemas.map import Map as MapSchema
from ..services.map_service import MapService


router = APIRouter()
map_service = MapService()


@router.post('/maps/', tags=['map'])
def create_map(map: MapSchema):
    map_object = map_service.create_map(map)
    return map_object


@router.get('/maps/', tags=['map'])
def get_all_maps():
    maps = map_service.get_maps()
    return maps


@router.get('/maps/{map_id}', tags=['map'])
def get_map(id: int):
    map_object = map_service.get_map_by_id(id)
    return map_object


@router.patch('/maps/{map_id}', tags=['map'])
def update_map(id: int, map: MapSchema):
    map_object = map_service.update_map(id, map)
    return map_object


@router.delete('/maps/{map_id}', tags=['map'])
def delete_map(id: int):
    map_object = map_service.delete_map_by_id(id)
    return map_object
