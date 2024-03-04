from microservices.aggregation_service.aggregation_service import run_server
from core.settings import AGGREGATION_GRPC_SERVER
import asyncio


if __name__ == '__main__':
    asyncio.run(run_server(AGGREGATION_GRPC_SERVER))
