"""
This module deals with models, specifying what each model needs and uses.
"""

from pydantic import BaseModel, Field


class Product(BaseModel):
    """
    The Product model contains information about a product that is part of an order, 
    such as its unique identifier, name, description, price, and quantity.
    """

    product_id: str | None = Field(..., description="Product ulid")
    name: str = Field(description="Product name")
    description: str | None = Field(description="Product description")
    price: float | None = Field(gt=0, description="The price must be greater than zero")
    quantity: int = Field(description="Product quantity")
