"""
MongoDB database connection file
"""

import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from dotenv import load_dotenv

load_dotenv()

def get_database_connection() -> AsyncIOMotorDatabase:
    """
    Creates and returns a connection to MongoDB.
    """
    mongo_url = os.getenv("MONGO_URL")
    database_name = os.getenv("MONGO_DATABASE_NAME")
    client = AsyncIOMotorClient(mongo_url)
    return client[database_name]
