from fastapi import APIRouter
from ..model.map import Map
from ..schemas.map import Map as MapSchema


router = APIRouter()


@router.post('/map/', tags=['map'])
async def create_map(map: MapSchema):
    db_map = Map(
        name='Test Map',
        latitude=10,
        longtitude=10,
        zoom_level=3
    )
    db_map.save()
    return db_map
