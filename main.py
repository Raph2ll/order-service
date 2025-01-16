"""
This module handles the initialisation of FastApi
"""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from configs.db_conn import get_database_connection
from storages.order_storage import OrderStorage
from services.order_service import OrderService
from routes.order_router import router


logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Method that handles FastApi configuration
    """
    db_connection = get_database_connection()

    order_storage = OrderStorage(db_conn=db_connection)
    order_service = OrderService(order_storage)

    yield {"order_service": order_service}
    logger.info("Shutdown application")

app = FastAPI(
    lifespan=lifespan,
    title="Order Service",
)

app.include_router(router)

@app.get("/health")
def health_check():
    """
    Healthy check to see if the application is working in a basic way
    """
    return {"status": "healthy"}
