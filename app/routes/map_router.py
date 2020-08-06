from fastapi import APIRouter
from ..schemas.map import Map as MapSchema
from ..services.map_service import MapService


router = APIRouter()
map_service = MapService()


@router.post('/map/', tags=['map'])
def create_map(map: MapSchema):
    map_object = map_service.create_map(map)
    return map_object


@router.get('/maps/', tags=['map'])
def get_all_maps():
    maps = map_service.get_maps()
    return maps


@router.get('/map/{id}')
def get_map(id: int):
    map_object = map_service.get_map_by_id(id)
    return map_object


@router.patch('/map/{id}')
def update_map(id: int):
    pass


@router.delete('/map/{id}')
def delete_map(id: int):
    map_object = map_service.delete_map_by_id(id)
    return map_object
