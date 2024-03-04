from grpc import aio
from protos import aggregate_pb2_grpc, aggregate_pb2
from microservices.aggregation_service import db_aggregation
from google.protobuf.json_format import MessageToDict
from logs.logs import init_logger

logger = init_logger(__name__)


class AggregationService(aggregate_pb2_grpc.AggregationServiceServicer):

    async def AggregateProduct(self, request, context):
        logger.info("AggregateProduct: request from product service received")
        product_dict = MessageToDict(request, preserving_proto_field_name=True)
        product_aggregated_status = await db_aggregation._aggregate_date(product=product_dict)
        logger.info("AggregateProduct: product has been aggregated")
        return aggregate_pb2.ProductToAggregateResponse(is_aggregated=product_aggregated_status)


async def run_server(address):
    # Здесь получаем асинхронный сервер
    server = aio.server()
    # Регистрируем сервер в aio сервере
    aggregate_pb2_grpc.add_AggregationServiceServicer_to_server(AggregationService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    logger.info("START SERVER AGGREGATION")
    await server.start()
    await server.wait_for_termination()
