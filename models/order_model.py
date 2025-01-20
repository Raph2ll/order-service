"""
This module deals with models, specifying what each model needs and uses.
"""

from typing import List
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from models.product_model import Product, ProductRequest
from models.customer_model import Customer


class Order(BaseModel):
    """
    The Order model contains information related to a customer's order, including the order ID,
    customer email, a list of products, the order status, and timestamps for when the order
    was created and last updated.
    """

    customer: Customer = Field(..., description="Customer details")
    products: List[Product] = Field(..., description="List of products in the order")
    active: bool = Field(default=True, description="Order status (active or inactive).")
    created_at: datetime = Field(
        default_factory=datetime.now, description="Order creation date."
    )
    updated_at: datetime | None = Field(default=None, description="Order update date.")


class OrderRequest(BaseModel):
    """
    Represents a customer's order request, including essential details such as the customer's email 
    and a list of products included in the order.
    """

    customer_email: EmailStr = Field(..., description="Valid customer email adress")
    products: List[ProductRequest] = Field(
        ..., description="List of products in the order"
    )


class CreateOrderResponse(BaseModel):
    """
    Represents the response for a created order, containing the unique order identifier.
    """

    order_id: str = Field(..., description="Unique order identifier in ObjectId format.")
