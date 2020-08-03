from fastapi import APIRouter
from ..model.map import Map
from ..schemas.map import Map as MapSchema


router = APIRouter()


@router.post('/map/', tags=['map'])
async def create_map(map: MapSchema):
    db_map = Map(
        0,
        name=map.name,
        latitude=map.latitude,
        longtitude=map.longitude,
        zoom_level=map.zoom
    )
    db_map.save()
    return db_map
