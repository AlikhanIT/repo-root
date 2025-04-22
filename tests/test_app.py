import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home_route():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"Hello from CI/CD!" in response.data
