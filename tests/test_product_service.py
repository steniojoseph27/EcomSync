import pytest
from app.services.product_service import ProductService
from app.models.product import Product

def test_create_product():
    service = ProductService()
    new_product = ProductService(name="Test", price=100)

    result = service.create_product(new_product)

    assert result.name == "Test"
    assert result.price == 100