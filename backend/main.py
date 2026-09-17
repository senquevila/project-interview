import json
import os

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

DATA_FILE = os.environ.get("DATA_FILE", "data.json")
STATIC_DIR = os.environ.get("STATIC_DIR", "../frontend/dist")

app = FastAPI()


@app.get("/api/data")
def get_data():
    with open(DATA_FILE) as f:
        return json.load(f)


app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
