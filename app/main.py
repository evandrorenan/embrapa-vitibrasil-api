import uvicorn
from fastapi import FastAPI
from app.api.wine_exports.v1.endpoints import wine_exports


app = FastAPI()
app.include_router(wine_exports.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
