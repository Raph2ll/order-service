"""
This module deals with models, specifying what each model needs and uses.
"""

from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    """
    Represents a customer with information such as name, email and status.
    """
    id: str = Field(..., description="Unique customer identifier in ULID format.")
    name: str = Field(..., description="Customer name")
    email: EmailStr = Field(..., description="Valid customer email adress")
