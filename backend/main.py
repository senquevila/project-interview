import json
import os

import uvicorn
from fastapi import FastAPI

DATA_FILE = os.environ.get("DATA_FILE", "data.json")

app = FastAPI()


@app.get("/data")
def get_data():
    with open(DATA_FILE) as f:
        return json.load(f)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
