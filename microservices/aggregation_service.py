from grpc import aio
from protos import aggregate_pb2_grpc, aggregate_pb2
from product import db_products
import google.protobuf.wrappers_pb2
from models.models import Product
from microservices.client import grpc_aggregation_client
from aggregation import db_aggregation
from google.protobuf.json_format import MessageToDict


class AggregationService(aggregate_pb2_grpc.AggregationServiceServicer):

    async def AggregateProduct(self, request, context):
        print("AggregateProduct")
        product_dict = MessageToDict(request, preserving_proto_field_name=True)
        product_aggregated_status = await db_aggregation._aggregate_date(product=product_dict)
        print("product_aggregated", product_aggregated_status)
        return aggregate_pb2.ProductToAggregateResponse(is_aggregated=product_aggregated_status)


async def run_server(address):
    # Здесь получаем асинхронный сервер
    server = aio.server()
    print('START SERVER AGGREGATION')
    # Регистрируем сервер в aio сервере
    aggregate_pb2_grpc.add_AggregationServiceServicer_to_server(AggregationService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    print('START SERVER AGGREGATION')
    await server.start()
    await server.wait_for_termination()
