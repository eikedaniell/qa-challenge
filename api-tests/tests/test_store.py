from conftest import BASE_URL

def test_place_order(api_client):
    order = {
        "id": 1,
        "petId": 1001,
        "quantity": 2,
        "status": "placed"
    }
    response = api_client.post(f"{BASE_URL}/store/order", json=order)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"

def test_find_order_by_id(api_client):
    response = api_client.get(f"{BASE_URL}/store/order/1")
    assert response.status_code == 200