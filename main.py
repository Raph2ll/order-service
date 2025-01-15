from fastapi import FastAPI
from configs.db_conn import get_database_connection
from storages.order_storage import OrderStorage
from models.order_model import Order
app = FastAPI()

db_connection = get_database_connection()

@app.get("/health")
def health_check():
    """
    Healthy check to see if the application is working in a basic way
    """
    return {"status": "healthy"}

@app.post("/v1/orders", response_model=Order)
async def create_purchase_order(order: Order):
    """
    Endpoint to create a new order.
    """
    order_storage = OrderStorage(db_connection)
    try:

        order_dict = order.model_dump()
        order_id = await order_storage.create_purchase_order(order_dict)
        return {"order_id": order_id}
    except ValueError as e:
        return {"error": str(e)}
