from microservices.task_service import run_server
from core.settings import TASK_GRPC_SERVER
import asyncio


if __name__ == '__main__':
    asyncio.run(run_server(TASK_GRPC_SERVER))
