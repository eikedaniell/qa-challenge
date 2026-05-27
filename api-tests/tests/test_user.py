from conftest import BASE_URL

def test_create_user(api_client):
    user = {
        "id": 101,
        "username": "joao_test",
        "firstName": "Joao",
        "lastName": "Silva",
        "email": "joao@test.com",
        "password": "123456"
    }
    response = api_client.post(f"{BASE_URL}/user", json=user)
    assert response.status_code == 200

def test_login_user(api_client):
    response = api_client.get(f"{BASE_URL}/user/login?username=joao_test&password=123456")
    assert response.status_code == 200
    assert "logged in" in response.text