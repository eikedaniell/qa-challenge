import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session