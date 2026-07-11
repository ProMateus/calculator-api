from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "1.0.3"


def test_calculate_add():
    response = client.post(
        "/calculate",
        json={
            "a": 5,
            "b": 7,
            "operation": "add"
        }
    )

    assert response.status_code == 200
    assert response.json()["result"] == 12
