def test_add_new_pet(api_client):
    pet_data = {
        "id": 1001,
        "name": "Doggie"  
        "status": "available"
    }
    response = api_client.post(f"{BASE_URL}/pet", json=pet_data)
    assert response == 200 