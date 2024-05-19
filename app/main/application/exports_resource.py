from fastapi import FastAPI

app = FastAPI()


@app.get("/exports")
def get_all_exports():
    return {"Hello": "World"}
