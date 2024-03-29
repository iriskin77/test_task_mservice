from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime, date


class ProductBase(BaseModel):

    unique_code: str = Field(validation_alias="УникальныйКодПродукта")
    number_batch: int = Field(validation_alias="НомерПартии")
    date_product: datetime = Field(validation_alias="ДатаПартии")

    model_config = ConfigDict(populate_by_name=True,)

    @field_validator("date_product", mode='after')
    @classmethod
    def datetime_to_timestamp(cls, value):
        return datetime.timestamp(value)


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
