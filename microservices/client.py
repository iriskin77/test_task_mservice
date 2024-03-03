import grpc
from protos import task_pb2_grpc, product_pb2_grpc, aggregate_pb2_grpc
from core.settings import TASK_GRPC_SERVER, PRODUCT_GRPC_SERVER, AGGREGATION_GRPC_SERVER


async def grpc_task_client():
    # Открываем канал и указываем, на каком порту
    channel = grpc.aio.insecure_channel(TASK_GRPC_SERVER)
    # Создаем и возвращаем клиент
    client = task_pb2_grpc.TaskServiceStub(channel)
    return client


async def grpc_product_client():
    # Открываем канал и указываем, на каком порту
    channel = grpc.aio.insecure_channel(PRODUCT_GRPC_SERVER)
    # Создаем и возвращаем клиент
    client = product_pb2_grpc.ProductServiceStub(channel)
    return client


async def grpc_aggregation_client():
    # Открываем канал и указываем, на каком порту
    channel = grpc.aio.insecure_channel(AGGREGATION_GRPC_SERVER)
    # Создаем и возвращаем клиент
    client = aggregate_pb2_grpc.AggregationServiceStub(channel)
    return client


