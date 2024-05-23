import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import wine_exports_routes, wine_imports_routes, wine_processing_routes, \
    wine_production_routes, wine_trades_routes

app = FastAPI()
app.include_router(wine_exports_routes.router, prefix="/api/v1")
app.include_router(wine_imports_routes.router, prefix="/api/v1")
app.include_router(wine_processing_routes.router, prefix="/api/v1")
app.include_router(wine_production_routes.router, prefix="/api/v1")
app.include_router(wine_trades_routes.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
