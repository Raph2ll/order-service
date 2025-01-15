"""
Module for managing Order data.
"""
from models.order_model import Order
from typing import List
from datetime import datetime


class OrderStorage:
    """
    Class responsible for managing operations in the 'orders' collection.
    """

    def __init__(self, db_conn):
        self.collection = db_conn["orders"]

    async def create_purchase_order(self, order_dict) -> str:
        """
        Inserts a new order into the 'orders' collection.
        """
        order = Order(**order_dict)

        order_data = order.model_dump()
        order_data["order_id"] = order.order_id
        order_data["created_at"] = order.created_at
        order_data["updated_at"] = None

        result = await self.collection.insert_one(order_data)
        return str(result.inserted_id)
