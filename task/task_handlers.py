from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from task import db_tasks
from task.schema import TaskChange, TaskGetPostPatch, ListTasksAdd


router_task = APIRouter()


@router_task.post("/")
async def create_task(item: TaskGetPostPatch):

    """"Эндпойнт добавления сменных заданий"""""

    try:
        res = await db_tasks._create_task(item=item)
        return res
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")


@router_task.get("/{id}")
async def get_task(id: int):

    """"Эндпойнт получения сменного задания (партии) по ID (primary key)"""""

    try:
        res = await db_tasks._get_task(id=id)

        return res
    except Exception as ex:
        raise HTTPException(status_code=500,
                            detail=f"Database error: {ex}")

@router_task.get("/")
async def get_task_list():
    tasks = await db_tasks._get_tasks_list()
    return tasks

@router_task.patch("/{id}", response_model=TaskGetPostPatch)
async def change_task(id: int, params_to_update: TaskChange):

    """"Эндпойнт изменения сменного задания (партии) по ID (primary key)"""""

    task = await db_tasks._get_task_by_id(id=id)

    if task is None:
        HTTPException(status_code=404, detail="Not found")

    if params_to_update == {}:
        raise HTTPException(status_code=422,
                            detail="At least one parameter for user update info should be provided")

    params = params_to_update.dict(exclude_none=True)

    try:
        res = await db_tasks._change_task(id=id, params_to_update=params)
        return res

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")


@router_task.delete("/{id}")
async def delete_task(id: int):
    task = await db_tasks._get_task_by_id(id=id)

    if task is None:
        HTTPException(status_code=404, detail="Not found")

    res = await db_tasks._delete_task(id=id)
    return res
