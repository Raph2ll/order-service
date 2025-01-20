"""
This module deals with models, specifying what each model needs and uses.
"""

from pydantic import BaseModel, Field


class Product(BaseModel):
    """
    The Product model contains information about a product that is part of an order,
    such as its unique identifier, name, description, price, and quantity.
    """

    id: str = Field(..., description="Product ulid")
    name: str = Field(description="Product name")
    description: str = Field(description="Product description")
    price: float = Field(gt=0, description="The price must be greater than zero")
    quantity: int = Field(description="Product quantity")


class ProductRequest(BaseModel):
    """
    Represents a product included in an order, containing key details such as the product's name 
    and the quantity being ordered.
    """

    name: str = Field(description="Product name")
    quantity: int = Field(description="Product quantity")
