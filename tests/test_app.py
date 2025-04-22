from app import app

def test_home_route():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"Hello from CI/CD!" in response.data
