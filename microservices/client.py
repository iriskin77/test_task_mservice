import grpc
from protos import task_pb2_grpc
from core.settings import TASK_GRPC_SERVER


async def grpc_task_client():
    # Открываем канал и указываем, на каком порту
    channel = grpc.aio.insecure_channel(TASK_GRPC_SERVER)
    # Создаем и возвращаем клиент
    client = task_pb2_grpc.TaskServiceStub(channel)
    return client


