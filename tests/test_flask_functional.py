import pytest
from garden.flaskr import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_notes_endpoint(client):
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "TEST"

