"""
MongoDB database connection file
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    """
    Creates and returns a connection to MongoDB.
    """

    client = MongoClient("mongodb://root:example@localhost:27017/orders")
    db = client['orders']
    return db
