import pytest
from app import app

@pytest.fixture
def client():
    # This sets up a mock client to test your Flask app without actually running the server
    with app.test_client() as client:
        yield client

def test_home_route(client):
    # This simulates a browser hitting your "/" route
    response = client.get('/')
    assert response.status_code == 200
    
    # This verifies the JSON response matches what your app outputs
    data = response.get_json()
    assert data["status"] == "running"
