from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, date


class ProductBase(BaseModel):

    unique_code: str = Field(validation_alias="УникальныйКодПродукта")
    number_batch_id: int = Field(validation_alias="НомерПартии")
    date_product: date = Field(validation_alias="ДатаПартии")

    model_config = ConfigDict(populate_by_name=True,)


class ListAddProducts(BaseModel):

    products: List[ProductBase]

    model_config = ConfigDict(populate_by_name=True,)


class ProductPost(ProductBase):

    is_aggregated: Optional[bool]
    aggregated_at: Optional[datetime]


class ProductAggregationRequest(BaseModel):

    task_id: int
    unique_code: str


class ProductAggregationResponse(BaseModel):

    unique_code: str | None = None
