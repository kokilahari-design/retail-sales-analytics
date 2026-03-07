import json
import pytest
from app import create_app


@pytest.fixture
def client():
    """
    Creates a Flask test client for API testing
    """
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

# Test API successfully inserts sale
def test_create_sale_success(client):
    """
    Test successful sale creation
    """

    payload = {
        "customer_id": 1,
        "product_id": 101,
        "product_name": "Laptop",
        "product_category": "Electronics",
        "quantity": 2,
        "price": 1000,
        "sale_datetime": "2025-03-21T10:00:00"
    }

    response = client.post(
        "/testing",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["message"] == "Sale recorded"

# Test API validation works
def test_create_sale_missing_field(client):
    """
    Test API validation when required field is missing
    """

    payload = {
        "customer_id": 1,
        "product_id": 101,
        "quantity": 2
    }

    response = client.post(
        "/testing",
        data=json.dumps(payload),
        content_type="application/json"
    )

    assert response.status_code == 400
    assert "error" in response.json

# Test API rejects invalid HTTP methods
def test_create_sale_invalid_method(client):
    """
    Test invalid HTTP method
    """

    response = client.get("/testing")

    assert response.status_code in [400, 405]
