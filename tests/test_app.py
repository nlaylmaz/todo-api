import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 500

def test_tasks_key_exists(client):
    response = client.get("/")
    data = response.get_json()

    assert "tasks" in data


def test_tasks_is_list(client):
    response = client.get("/")
    data = response.get_json()

    assert isinstance(data["tasks"], list)

def test_tasks_not_empty(client):
    response = client.get("/")
    data = response.get_json()

    assert len(data["tasks"]) >  0

def test_not_found(client):
    response = client.get("/olmayan-sayfa")

    assert response.status_code == 404

def test_tasks_are_strings(client):
    response = client.get("/")
    data = response.get_json()

    for task in data["tasks"]:
        assert isinstance(task, str)
