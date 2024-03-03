from datetime import datetime
from models.models import Task, Product

from product.schema import ListAddProducts, ProductAggregationRequest, ProductBase
from fastapi import HTTPException
from task.db_tasks import _get_task_by_id
from google.protobuf.json_format import MessageToDict


# ================ Aggregation data ================


async def _aggregate_date(product) -> bool:

    product_aggregated = await Product.update({'is_aggregated': True, 'aggregated_at': datetime.now()}).\
        where(Product.unique_code == product['product']['unique_code']).returning(Product.is_aggregated)

    return product_aggregated[0]['is_aggregated']
