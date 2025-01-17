import httpx
import logging
from models.order_model import Order, OrderRequest, CreateOrderResponse
from models.product_model import Product
from models.customer_model import Customer

from storages.order_storage import OrderStorage


class OrderService:
    """
    Class for handling business logic related to orders.
    """

    def __init__(self, storage: OrderStorage):
        self.storage = storage
        # Passar para o construtor dps:
        self.logger = logging.getLogger(__name__)
        self.customer_api_url = "http://localhost:6789"
        self.product_api_url = "http://localhost:8000"

    async def fetch_customer_data(self, customer_email: str):
        """
        Fetches customer data (ID, name, surname) by email from an external API.
        """

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.customer_api_url}/customers/email/{customer_email}")

            response.raise_for_status()
            customer_data = response.json()
            self.logger.info(f"Customer_data: {customer_data}")
            if not customer_data:
                raise ValueError("Customer not found.")
            return customer_data

    async def fetch_product_data(self, product_name: str):
        """
        Fetches product data (price, description) by product name from an external API.
        """

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.product_api_url}/products/name/{product_name}")
            response.raise_for_status()
            product_data = response.json()
            self.logger.info(f"Product_data: {product_data}")
            if not product_data:
                raise ValueError("Product not found.")
            return product_data

    async def create_purchase_order(self, order_request: OrderRequest) -> CreateOrderResponse:
        """
        Create a new purchase order.
        """

        if not order_request.customer_email:
            raise ValueError("Customer email is required.")

        if not order_request.products or len(order_request.products) == 0:
            raise ValueError("At least one product is required.")

        customer_data = await self.fetch_customer_data(order_request.customer_email)

        products_with_details = []
        for product in order_request.products:
            # Esse fetch fica só no GET ?
            product_data = await self.fetch_product_data(product.name)
            products_with_details.append(
                Product(
                    id=product_data["id"],
                    name=product.name,
                    description=product_data["description"],
                    price=product_data["price"],
                    # Lembrar de validar o quantity == | < product_data["quantity"]
                    quantity=product.quantity,
                )
            )

        order = Order(
            customer=Customer(
                customer_id=customer_data["id"],
                name=customer_data["name"],
                email=order_request.customer_email,
            ),
            products=products_with_details,
            updated_at=None,
        )

        await self.storage.create_purchase_order(order.model_dump())
        return order.order_id
