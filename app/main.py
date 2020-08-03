from fastapi import FastAPI
from .routes import map_router

app = FastAPI()
app.include_router(map_router.router)


@app.get('/ping')
def ping():
    return {'status': 'alive'}
