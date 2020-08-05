from fastapi import FastAPI
from .routes import map_router
from .model.map import Map
from .model.map_point import MapPoint


Map.create_table()
MapPoint.create_table()


app = FastAPI()
app.include_router(map_router.router)


@app.get('/ping')
def ping():
    return {'status': 'alive'}
