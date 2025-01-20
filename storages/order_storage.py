"""
Module for managing Order data.
"""

from pymongo.database import Database
from models.order_model import Order


class OrderStorage:
    """
    Class responsible for managing operations in the 'orders' collection.
    """

    def __init__(self, db_conn: Database):
        self.collection = db_conn["orders"]

    def create_purchase_order(self, order_data: Order) -> str:
        """
        Save a new order to the MongoDB database and return the generated _id.
        """
        result = self.collection.insert_one(order_data)

        return str(result.inserted_id)
