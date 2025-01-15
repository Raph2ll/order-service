"""
This module deals with models, specifying what each model needs and uses.
"""

from typing import List
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
import ulid
from models.product_model import Product


class Order(BaseModel):
    """
    The Order model contains information related to a customer's order, including the order ID, 
    customer email, a list of products, the order status, and timestamps for when the order 
    was created and last updated.
    """

    order_id: str = Field(
        default_factory=lambda: str(ulid.new()),
        description="Unique order identifier in ULID format.",
    )
    customer_email: EmailStr = Field(..., description="Valid customer email adress")
    products: List[Product] = Field(..., description="List of products in the order")
    active: bool = Field(
        default=True, description="Order status (active or inactive)."
    )
    created_at: datetime = Field(
        default_factory=datetime.now, description="Order creation date."
    )
    updated_at: datetime | None = Field(
        default=None, description="Order update date."
    )
