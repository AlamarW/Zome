import pytest
import json
from garden.flaskr import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_notes_endpoint(client):
    response = client.get("/note")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "TEST"


def test_create_note_success(client):
    """Test successful note creation with valid data"""
    payload = {
        "name": "My Test Note",
        "text": "This is a sample note about machine learning and machine intelligence.",
    }

    response = client.post(
        "/note", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 201
    response_data = json.loads(response.data)

    # Check basic fields
    assert response_data["name"] == "My Test Note"
    assert response_data["text"] == payload["text"]
    assert "id" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data
    assert response_data["high_frequency_words"] == {"machine": 2}
    assert response_data["themes"] == ["sample", "note", "machine"]

def test_get_note_by_name(client):
    pass
