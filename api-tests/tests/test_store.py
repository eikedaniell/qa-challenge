def test_place_order(api_client):
    response = api_client.post(f"{BASE_URL}/store/orde", json=order)  
    assert response.status_code == 200