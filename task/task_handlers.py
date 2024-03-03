from fastapi import APIRouter, Depends, HTTPException
from pydantic import typing
from grpc.aio import AioRpcError
from microservices.client import grpc_task_client
from task import db_tasks
from task.schema import TaskChange, TaskGetPostPatch, ListTasksAdd, CreateTask
from protos import task_pb2_grpc, task_pb2
from google.protobuf.json_format import MessageToDict
from fastapi.responses import JSONResponse
from models.models import Task
from datetime import datetime
import time


router_task = APIRouter()


@router_task.post("/", response_model=CreateTask)
async def create_task(item: CreateTask, client: typing.Any = Depends(grpc_task_client)):

    """"Эндпойнт добавления сменных заданий"""""

    try:

        print(item.dict())
        data = item.dict()
        task = await client.CreateTask(task_pb2.CreateTaskRequest(**data))
        return JSONResponse(MessageToDict(task, preserving_proto_field_name=True))
        #data = db_tasks.timestamp_to_datetime(item.dict())
        #res = await Task.insert(Task(**data))
        #return item.dict()
    except AioRpcError as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex.details()}")


@router_task.get("/{id}")
async def get_task(id: int, client: typing.Any = Depends(grpc_task_client)) -> JSONResponse:

    """"Эндпойнт получения сменного задания (партии) по ID (primary key)"""""

    try:
        task = await client.GetTask(task_pb2.GetTaskRequest(id=id))

        return JSONResponse(MessageToDict(task, preserving_proto_field_name=True))

    except Exception as ex:
        raise HTTPException(status_code=500,
                            detail=f"Database error: {ex}")


@router_task.get("/")
async def get_task_list(client: typing.Any = Depends(grpc_task_client)) -> JSONResponse:
    try:
        tasks = await client.GetTaskList(task_pb2.GetTaskListRequest())
        print(tasks)
        return JSONResponse(MessageToDict(tasks))
    except AioRpcError as ex:
        raise HTTPException(status_code=404, detail=f"Error: {ex.details()}")


@router_task.patch("/", response_model=TaskGetPostPatch)
async def change_task(params_to_update: TaskChange, client: typing.Any = Depends(grpc_task_client)):

    """"Эндпойнт изменения сменного задания (партии) по ID (primary key)"""""

    # task = await db_tasks._get_task_by_id(id=id)
    #
    # if task is None:
    #     HTTPException(status_code=404, detail="Not found")

    if params_to_update == {}:
        raise HTTPException(status_code=422,
                            detail="At least one parameter for user update info should be provided")

    params = params_to_update.dict(exclude_none=True)
    #data = db_tasks.datetime_to_timestamp(params)
    #data['id'] = id
    print(params)
    try:
        #print(data)
        task_updated = await client.UpdateTask(task_pb2.UpdateTaskRequest(**params))
        #res = await db_tasks._change_task(id=id, params_to_update=params)
        #return res
        return JSONResponse(MessageToDict(task_updated))

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")


@router_task.delete("/{id}")
async def delete_task(id: int, client: typing.Any = Depends(grpc_task_client)):
    task = await db_tasks._get_task_by_id(id=id)

    if task is None:
        HTTPException(status_code=404, detail="Not found")

    task_deleted_id = await client.DeleteTask(task_pb2.DeleteTaskRequest(id=id))
    return JSONResponse(MessageToDict(task_deleted_id))
