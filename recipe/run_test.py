import platform
import subprocess

import fastapi
from fastapi import FastAPI, dependencies, middleware, openapi, security

subprocess.run(["pip", "check"])

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


# Skip tests on s390x because of missing httpx package
if platform.machine() != "s390x":
    from fastapi.testclient import TestClient

    client = TestClient(app)

    def test_read_main():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
