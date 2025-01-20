"""
Tests for OrderStorage tabase interactions.
"""

from unittest.mock import MagicMock
from datetime import datetime
import pytest
import ulid
from pytest import fixture
from storages.order_storage import OrderStorage
from models.order_model import Order
from models.product_model import Product
from models.customer_model import Customer



@fixture(name="mongo_collection")
def fixture_mongo_collection():
    """
    Creates a mock MongoDB collection for database interactions.
    """
    return MagicMock()


@fixture(name="storage")
def fixture_storage(mongo_collection: MagicMock) -> OrderStorage:
    """
    Creates an OrderStorage instance with a mock MongoDB collection.
    """
    return OrderStorage(mongo_collection)


@fixture(name="customer_data")
def fixture_customer_data():
    """
    Creates a mock customer object for the order.
    """
    return Customer(
        customer_id="0123456789ABCDEFGHJKMNPQRSTVWXYZ",
        name="John Doe",
        email="john.doe@example.com"
    )


@fixture(name="product_data")
def fixture_product_data():
    """
    Creates a mock product object for the order.
    """
    return Product(
        id="0123456789ABCDEFGHJKMNPQRSTVWXYZ",
        name="Product 1",
        description="A description of Product 1",
        price=100.0,
        quantity=2,
    )


@fixture(name="order_data")
def fixture_order_data(customer_data, product_data):
    """
    Creates a mock order object that includes customer data and product data.
    """
    return Order(
        customer=customer_data,
        products=[product_data],
        active=True,
        created_at=datetime(2024, 1, 1, 12, 0, 0),
        updated_at=datetime(2024, 1, 2, 15, 30, 0),
    )


def test_create_purchase_order(storage, mongo_collection, order_data):
    """
    Test that `create_purchase_order` inserts a new order into MongoDB
    and returns the generated order ID.
    """
    mock_inserted_id = ulid.new()

    mongo_collection.insert_one.return_value.inserted_id = mock_inserted_id

    result = storage.create_purchase_order(order_data)

    assert result == str(mock_inserted_id)

    mongo_collection.insert_one.assert_called_once_with(order_data)
