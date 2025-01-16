"""
Module for managing Order data.
"""

from pymongo.database import Database
from models.order_model import Order
from typing import List
from datetime import datetime


class OrderStorage:
    """
    Class responsible for managing operations in the 'orders' collection.
    """

    def __init__(self, db_conn: Database):
        self.collection = db_conn["orders"]

    async def create_purchase_order(self, order_data: dict) -> str:
        """
        Save a new order to the MongoDB database.
        """
        result = await self.collection.insert_one(order_data)

        return str(result.inserted_id)
