from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from product.schema import ListAddProducts, ProductAggregationRequest, ProductAggregationResponse
from product import db_products
from microservices.client import grpc_product_client
from protos import product_pb2, product_pb2_grpc
from google.protobuf.json_format import MessageToDict
from fastapi.responses import JSONResponse
from grpc.aio import AioRpcError

router_product = APIRouter()


@router_product.post("/")
async def product_create(items: ListAddProducts, client: Any = Depends(grpc_product_client)):


    """"Эндпойнт добавления продукции для сменного задания (партии)"""""

    try:
        print(items.dict())
        is_products_added = await client.CreateProducts(product_pb2.CreateProductRequest(**items.dict()))
        #res = await db_products._product_create(items=items)
        #return res
        return JSONResponse(MessageToDict(is_products_added))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")


@router_product.get("/")
async def get_products_list(client: Any = Depends(grpc_product_client)):
    try:
        products = await client.GetProductsList(product_pb2.GetProductsListResponse())
        return JSONResponse(MessageToDict(products))
    except AioRpcError as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex.details()}")


@router_product.patch("/", response_model=ProductAggregationResponse)
async def aggregate(item: ProductAggregationRequest):

    """"Эндпойнт "аггрегации" продукции"""""

    try:
        res = await db_products._aggregate_date(item=item)

        return res
    except AioRpcError as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex.details()}")
