import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_hello(client):
    resp = client.get("/api/hello")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello from DevOps API"}


def test_list_items_empty(client):
    resp = client.get("/api/items")
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)


def test_create_item(client):
    resp = client.post("/api/items", json={"name": "banana"})
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["name"] == "banana"
    assert "id" in body

    # Confirm it shows up in the list
    resp2 = client.get("/api/items")
    items = resp2.get_json()
    assert any(item["name"] == "banana" for item in items)


def test_create_item_missing_name(client):
    resp = client.post("/api/items", json={})
    assert resp.status_code == 400
    assert "error" in resp.get_json()
