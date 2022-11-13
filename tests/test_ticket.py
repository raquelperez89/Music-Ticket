from fastapi.testclient import TestClient

from main import app


ticket = TestClient(app = app)


def test_index():
    response = ticket.get("/all")
    assert response.status_code == 200
