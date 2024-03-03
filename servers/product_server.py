from microservices.product_service import run_server
from core.settings import PRODUCT_GRPC_SERVER
import asyncio


if __name__ == '__main__':
    asyncio.run(run_server(PRODUCT_GRPC_SERVER))
