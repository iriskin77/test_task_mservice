from grpc import aio
from protos import product_pb2_grpc, product_pb2
from product import db_products


class ProductService(product_pb2_grpc.ProductServiceServicer):

    async def CreateProducts(self, request, context):
        print("CreateProducts")
        print(request)
        products = await db_products._product_create(request)
        return product_pb2.CreateProductResponse(products=products)


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
