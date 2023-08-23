import subprocess

import fastapi
from fastapi import FastAPI, dependencies, middleware, openapi, security
from fastapi.testclient import TestClient


subprocess.run(["pip", "check"])

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
