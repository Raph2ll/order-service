"""
This module deals with models, specifying what each model needs and uses.
"""

from datetime import datetime
from pydantic import BaseModel, Field, model_validator


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
    The Product model contains information about a product that is part of an order,
    such as its unique identifier, name, description, price, and quantity.
    """

    name: str = Field(description="Product name")
    quantity: int = Field(description="Product quantity")

    # @model_validator(mode="before")
    # def check_product_quantities(self, values):
    #     """
    #     Validator to ensure that the quantity of products is always greater than 0.
    #     """
    #     products = values.get("products", [])
    #     if any(product.get("quantity", 0) <= 0 for product in products):
    #         raise ValueError("Product quantity must be greater than 0.")
    #     return values

