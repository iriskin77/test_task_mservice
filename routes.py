from fastapi import APIRouter
from api_gateway import product_handlers, task_handlers

routes = APIRouter()


routes.include_router(router=task_handlers.router_task, prefix="/task")
routes.include_router(router=product_handlers.router_product, prefix="/product")
