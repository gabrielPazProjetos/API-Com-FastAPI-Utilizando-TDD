from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products", json={"name": "TV", "price": 3000})
    assert response.status_code == 201
    assert "id" in response.json()

def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filter_products():
    response = client.get("/products/filter?min_price=1000&max_price=5000")
    assert response.status_code == 200
