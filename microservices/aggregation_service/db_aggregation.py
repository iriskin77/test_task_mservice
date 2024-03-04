from datetime import datetime
from microservices.task_service.models.models import Product


# ================ Aggregation data ================


async def _aggregate_date(product) -> bool:

    product_aggregated = await Product.update({'is_aggregated': True, 'aggregated_at': datetime.now()}).\
        where(Product.unique_code == product['product']['unique_code']).returning(Product.is_aggregated)

    return product_aggregated[0]['is_aggregated']
