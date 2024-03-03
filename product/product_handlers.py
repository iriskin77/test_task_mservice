from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from product.schema import ListAddProducts, ProductAggregationRequest, ProductAggregationResponse
from product import db_products
from microservices.client import grpc_product_client
from protos import product_pb2, product_pb2_grpc
from google.protobuf.json_format import MessageToDict
from fastapi.responses import JSONResponse

router_product = APIRouter()


@router_product.post("/")
async def product_create(items: ListAddProducts, client: Any = Depends(grpc_product_client)):


    """"Эндпойнт добавления продукции для сменного задания (партии)"""""

    try:
        print(items.dict())
        products = await client.CreateProducts(product_pb2.CreateProductRequest(**items.dict()))
        #res = await db_products._product_create(items=items)
        #return res
        return JSONResponse(MessageToDict(products))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")


@router_product.patch("/", response_model=ProductAggregationResponse)
async def aggregate(item: ProductAggregationRequest):

    """"Эндпойнт "аггрегации" продукции"""""

    try:
        res = await db_products._aggregate_date(item=item)

        return res
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
