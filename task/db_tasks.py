from models.models import Task, Product
from datetime import datetime, date
from task.schema import TaskChange, TaskFilter, TaskFilterRes, TaskGetPostPatch, ListTasksAdd
from google.protobuf.json_format import MessageToDict
from task.schema import TaskGetPostPatch
import time

# ==================Post endpoint. Create a task==================


async def _create_task(request_from_task_api):
    dct = MessageToDict(request_from_task_api, preserving_proto_field_name=True)
    dict_from_message = timestamp_to_datetime(dct)
    print(dict_from_message)
    task_by_batch_date = await get_task_by_batch_date(date_batch=dict_from_message['date_batch'])

    if not dict_from_message['is_closed']:
        dict_from_message['closed_at'] = None

    print(dict_from_message)
    # if task_by_batch_date is not None:
    #
    #     res = await Task.update(dict_from_message).where(
    #         (Task.number_batch == dict_from_message['number_batch']) & (Task.date_batch == dict_from_message['date_batch'])
    #     ).returning(Task.id)
    #     print('RES', res)
    #     return res # id

    res = await Task.insert(Task(**dict_from_message))# [{'id': int}]
    return res[0]['id']


async def get_task_by_batch_date(date_batch):
    print('date_batch', date_batch)
    task = Task.select().where(Task.date_batch == date_batch)
    if task:
        return task


async def _get_task(id: int):

    task = await _get_task_by_id(id=id)
    res = datetime_to_timestamp(task)

    #res = await Product.select(Product.unique_code, Product.number_batch.task)
    #products = await Product.select(Product.number_batch, Product.all_columns())
    #task['products'] = products

    return res


async def _get_tasks_list():
    res = []
    tasks = await Task.select()
    for task in tasks:
        res.append(datetime_to_timestamp(task))
    return res


async def _get_task_by_id(id: int):

    task = await Task.select().where(Task.id == id).first()
    if task:
        return task
    return None
#
#
# # ================ Patch endpoint, Change a task =================
#
#
async def _change_task(params_to_update):

    dct = MessageToDict(params_to_update, preserving_proto_field_name=True)
    dict_from_message = timestamp_to_datetime(dct)

    is_closed = dict_from_message.get('is_closed', None)

    # Если статус закрытия партии меняется на True, то в closed_at необходимо выставить текущий datetime
    if is_closed is not None and is_closed:
        dict_from_message['closed_at'] = datetime.now()

    # если наоборот -- то null
    if is_closed is not None and not is_closed:
        dict_from_message['closed_at'] = None

    dict_from_message['id'] = int(dict_from_message['id'])
    id = dict_from_message['id']
    task_updated = await Task.update(dict_from_message).where(Task.id == id).returning(Task.id)

    return task_updated


async def _delete_task(id: int):
    task = await Task.delete().where(Task.id == id).returning(Task.id)
    return task


def timestamp_to_datetime(items: dict):
    res = {}
    for item in items.items():
        if isinstance(item[1], float):
            res[item[0]] = datetime.fromtimestamp(item[1])
        else:
            res[item[0]] = item[1]
    res['number_batch'] = int(res['number_batch'])
    return res


def datetime_to_timestamp(items: dict):
    res = {}
    for item in items.items():
        if isinstance(item[1], datetime):
            res[item[0]] = datetime.timestamp(item[1])
        else:
            res[item[0]] = item[1]
    res['number_batch'] = int(res['number_batch'])
    return res
