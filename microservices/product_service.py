from grpc import aio
from protos import product_pb2_grpc, product_pb2, aggregate_pb2
from product import db_products
from microservices.client import grpc_aggregation_client
from datetime import datetime
from models.models import Product


class ProductService(product_pb2_grpc.ProductServiceServicer):

    async def CreateProducts(self, request, context):
        print("CreateProducts")
        print(request)
        try:
            await db_products._product_create(request)
        except Exception as ex:
            print(f"Logging, {ex}")
            return product_pb2.CreateProductResponse(status=False)
        else:
            print('success', True)
            return product_pb2.CreateProductResponse(status=True)

    async def GetProductsList(self, request, context):
        print("GetProductsList")
        try:
            products = await db_products.get_products()
        except Exception as ex:
            print(f"Logging, {ex}")
            #return product_pb2.GetProductsListResponse(products=products)
        else:
            print('success', True)
            return product_pb2.GetProductsListResponse(products=products)

    async def AggregateProduct(self, request, context):
        print("AggregateProduct")
        print(request.unique_code)
        pr = await db_products.get_product_by_unique_code(unique_code=request.unique_code)
        print('pr', pr)
        if pr is not None:

            print('pr_timestamp', pr)

            client = await grpc_aggregation_client()

            product_aggregated_status = await client.AggregateProduct(
                aggregate_pb2.ProductToAggregateRequest(product=pr)
            )
            print(product_aggregated_status.is_aggregated)
            return product_pb2.AggregateResponse(is_aggregated=product_aggregated_status.is_aggregated)

        else:
            return product_pb2.AggregateResponse(is_aggregated=False)


async def run_server(address):
    # Здесь получаем асинхронный сервер
    server = aio.server()
    print('START SERVER PRODUCT')
    # Регистрируем наш Todo сервер в aio сервере
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    print('START SERVER PRODUCT')
    await server.start()
    await server.wait_for_termination()
