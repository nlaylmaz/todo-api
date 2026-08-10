from app import app

def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

def test_tasks_key_exists():
    client = app.test_client()
    response = client.get("/")

    data = response.get_json()

    assert "tasks" in data


def test_tasks_is_list():
    client = app.test_client()
    response = client.get("/")

    data = response.get_json()

    assert isinstance(data["tasks"], list)

def test_tasks_not_empty():
    client = app.test_client()
    response = client.get("/")

    data = response.get_json()

    assert len(data["tasks"]) ==  0

def test_not_found():
    client = app.test_client()
    response = client.get("/olmayan-sayfa")

    assert response.status_code == 404
