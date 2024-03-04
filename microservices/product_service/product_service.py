from grpc import aio
from logs.logs import init_logger
from protos import product_pb2_grpc, product_pb2, aggregate_pb2
from microservices.product_service import db_products
from microservices.client import grpc_aggregation_client


logger = init_logger(__name__)


class ProductService(product_pb2_grpc.ProductServiceServicer):

    async def CreateProducts(self, request, context):
        logger.info("CreateProducts: request from api has been received")
        try:
            await db_products._product_create(request)
        except Exception as ex:
            logger.warning(f"CreateProducts: database error: {str(ex)}")
            return product_pb2.CreateProductResponse(status=False)
        else:
            logger.info(f"CreateProducts: products have been added into db")
            return product_pb2.CreateProductResponse(status=True)

    async def GetProductsList(self, request, context):
        logger.info("GetProductsList: request from api has been received")
        try:
            products = await db_products.get_products()
        except Exception as ex:
            logger.warning(f"CreateProducts: database error: {str(ex)}")
        else:
            logger.info("GetProductsList: list products retrieved from db")
            return product_pb2.GetProductsListResponse(products=products)

    async def AggregateProduct(self, request, context):
        logger.info("AggregateProduct: request from api has been received")
        pr = await db_products.get_product_by_unique_code(unique_code=request.unique_code)
        if pr is not None:

            logger.info("AggregateProduct: product for aggregation has been retrieved")

            client = await grpc_aggregation_client()

            product_aggregated_status = await client.AggregateProduct(
                aggregate_pb2.ProductToAggregateRequest(product=pr)
            )

            return product_pb2.AggregateResponse(is_aggregated=product_aggregated_status.is_aggregated)

        else:
            logger.warning("AggregateProduct: product for aggregation was not found")
            return product_pb2.AggregateResponse(is_aggregated=False)


async def run_server(address):
    # Здесь получаем асинхронный сервер
    server = aio.server()
    logger.info("START SERVER PRODUCT")
    # Регистрируем наш сервер в aio сервере
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    await server.start()
    await server.wait_for_termination()
