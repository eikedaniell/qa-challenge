import pytest
from conftest import BASE_URL

def test_add_new_pet(api_client):
    pet_data = {
        "id": 1001,
        "name": "Doggie",
        "status": "available"
    }
    response = api_client.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Doggie"

def test_find_pet_by_id(api_client):
    response = api_client.get(f"{BASE_URL}/pet/1001")
    assert response.status_code == 200
    assert response.json()["id"] == 1001

def test_update_pet(api_client):
    updated = {"id": 1001, "name": "Max", "status": "sold"}
    response = api_client.put(f"{BASE_URL}/pet", json=updated)
    assert response.status_code == 200
    assert response.json()["name"] == "Max"

def test_delete_pet(api_client):
    response = api_client.delete(f"{BASE_URL}/pet/1001")
    assert response.status_code == 200