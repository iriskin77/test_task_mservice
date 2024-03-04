from datetime import datetime
from models.models import Task, Product
from logs.logs import init_logger
from google.protobuf.json_format import MessageToDict

logger = init_logger(__name__)


async def _product_create(items) -> None:
    logger.info("fn _product_create: inserting product object into db has been started")
    dict_product = MessageToDict(items, preserving_proto_field_name=True)
    products = datetime_to_timestamp(products=dict_product['products'])
    products_to_add = []
    for new_product in products:

        #print(new_product.date_product)
        task = await get_task_by_num_date_batch(number_batch=new_product['number_batch'],
                                                date_product=new_product['date_product'])

        #print(task)

        product = await get_product_by_unique_code(unique_code=new_product['unique_code'])
        #print(product)

        # Если продукция передана с несуществующей партией (== None),
        # т.е. нет сменного задания с указаным номером партии и датой партии, то данную продукцию можно игнорировать.

        #if task is not None:
            # Если переданная продукция с данным уникальным кодом уже существует, то ее можно игнорировать.
            #print(new_product)
            #if product is None:

                #dict_product = Product(**new_product.dict())
        products_to_add.append(new_product)
                #print(new_product)

        await Product.insert(Product(**new_product))
        logger.info("fn _product_create: product object into db has been inserted successfully")


async def get_products():

    products = await Product.select()
    res = datetime_to_timestamp(products)
    return res


async def get_task_by_num_date_batch(number_batch,
                                     date_product):

    task = await Task.select().where(
        (Task.number_batch == number_batch) & (Task.date_batch == date_product)
    ).first()

    if task:
        return task
    return None


async def get_product_by_unique_code(unique_code):

    product = await Product.select().where(Product.unique_code == unique_code).first()
    if product:
        return product
    return None


def datetime_to_timestamp(products: list[dict]):
    for product in products:
        product['date_product'] = datetime.fromtimestamp(product['date_product'])
        product['number_batch'] = int(product['number_batch'])
    return products


def timestamp_to_datetime(products: list[dict]):
    for product in products:
        product['date_product'] = datetime.timestamp(product['date_product'])
    return products


async def get_product_by_unique_code(unique_code: str):
    product = await Product.select().where(Product.unique_code == unique_code).first()

    if product:
        product['aggregated_at'] = datetime.timestamp(product['aggregated_at'])
        product['date_product'] = datetime.timestamp(product['date_product'])
        return product

