from models.models import Task, Product
from datetime import datetime, date
from task.schema import TaskChange, TaskFilter, TaskFilterRes, TaskGetPostPatch, ListTasksAdd
from google.protobuf.json_format import MessageToDict
from task.schema import TaskGetPostPatch
import time

# ==================Post endpoint. Create a task==================


async def _create_task(request_from_task_api):
    dict_from_message = MessageToDict(request_from_task_api, preserving_proto_field_name=True)
    dct = timestamp_to_datetime(dict_from_message)
    task_by_batch_date = await get_task_by_batch_date(date_batch=dct['date_batch'])

    if not dct['is_closed']:
        dct['closed_at'] = None

    if task_by_batch_date is not None:

        res = await Task.update(dct).where(
            (Task.number_batch == dct['number_batch']) & (Task.date_batch == dct['date_batch'])
        ).returning(Task.id)

        return res # id

    res = await Task.insert(Task(**dct)) # [{'id': int}]
    return res


def datetime_to_timestamp(dct: dict):
    print("datetime_to_timestamp")
    """Переводит datetime в timestamp(float). Необходимо для передачи по grpc по proto файлам"""
    res = {}
    for item in dct.items():

        if isinstance(item[1], datetime) or isinstance(item[1], date):
            #datetime.fromtimestamp(d['date_batch'])
            res[item[0]] = time.mktime(item[1].timetuple())
            #time.mktime(item[1].timetuple())
        else:
            res[item[0]] = item[1]

    res['number_batch'] = int(res['number_batch'])
    return res


def timestamp_to_datetime(dct: dict):
    print("timestamp_to_datetime")
    """Переводит timestamp в datetime. Необходимо для добавления в БД"""
    res = {}
    for item in dct.items():

        if isinstance(item[1], float):
            print(item[1])
            res[item[0]] = datetime.fromtimestamp(item[1])
        else:
            res[item[0]] = item[1]

    res['number_batch'] = int(res['number_batch'])
    return res


async def get_task_by_batch_date(date_batch):
    print('date_batch', date_batch)
    task = Task.select().where(Task.date_batch == date_batch)
    if task:
        return task


async def _get_task(id: int):

    task = await _get_task_by_id(id=id)

    #res = await Product.select(Product.unique_code, Product.number_batch.task)
    #products = await Product.select(Product.number_batch, Product.all_columns())
    #task['products'] = products
    res = datetime_to_timestamp(task)

    return res


async def _get_tasks_list():
    res = []
    tasks = await Task.select()
    for task in tasks:
        dct = datetime_to_timestamp(task)
        res.append(dct)
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

    dict_from_message = MessageToDict(params_to_update, preserving_proto_field_name=True)
    dct = timestamp_to_datetime(dict_from_message)

    is_closed = dct.get('is_closed', None)

    # Если статус закрытия партии меняется на True, то в closed_at необходимо выставить текущий datetime
    if is_closed is not None and is_closed:
        dct['closed_at'] = datetime.now()

    # если наоборот -- то null
    if is_closed is not None and not is_closed:
        dct['closed_at'] = None

    dct['id'] = int(dct['id'])
    id = dct['id']
    task_updated = await Task.update(dct).where(Task.id == id).returning(Task.id)

    return task_updated


async def _delete_task(id: int):
    task = await Task.delete().where(Task.id == id).returning(Task.id)
    return task

