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

    client = MongoClient(os.getenv("MONGO_URL"))
    db = client[os.getenv("MONGO_DB")]
    return db
