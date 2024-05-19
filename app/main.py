from fastapi import FastAPI

from app.api.wine_exports.v1.endpoints import wine_exports

app = FastAPI()


app.include_router(wine_exports.router, prefix="/api/v1")
