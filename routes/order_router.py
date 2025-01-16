"""
This module handles order routes.
"""

import logging
from typing import Annotated
from fastapi import APIRouter, Depends, Request
from models.order_model import Order, OrderRequest
from services.order_service import OrderService


router = APIRouter()
logger = logging.getLogger(__name__)


def get_order_service(request: Request):
    """
    Retrieves the order service instance from the request state.
    """
    return request.state.order_service


ServiceDep = Annotated[OrderService, Depends(get_order_service)]


@router.post("/v1/orders", response_model=Order)
async def create_purchase_order(request: OrderRequest, service: ServiceDep):
    """
    Endpoint to create a new order.
    """
    try:
        logger.info("Creatind a new order=%s", request)
        order = await service.create_purchase_order(request)
        return {"order_id": order}
    except ValueError as e:
        return {"error": str(e)}
