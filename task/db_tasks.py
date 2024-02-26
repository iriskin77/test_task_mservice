from models.models import Task, Product
from datetime import datetime
from task.schema import TaskChange, TaskFilter, TaskFilterRes, TaskGetPostPatch, ListTasksAdd

# ==================Post endpoint. Create a task==================


async def _create_task(item: TaskGetPostPatch):

    task_by_batch_date = await get_task_by_batch_date(date_batch=item.date_batch)

    if not item.is_closed:
        item.closed_at = None

    if task_by_batch_date is not None:

        new_task_to_update = item.dict(exclude={'number_batch', 'date_batch'})

        res = await Task.update(new_task_to_update).where(
            (Task.number_batch == item.number_batch) & (Task.date_batch == item.date_batch)
        ).returning(Task.id)

    return res


async def get_task_by_batch_date(date_batch):
    task = Task.select().where(Task.date_batch == date_batch)
    if task:
        return task
    return None


async def _get_task(id: int):

    task = await _get_task_by_id(id=id)

    #res = await Product.select(Product.unique_code, Product.number_batch.task)
    products = await Product.select(Product.number_batch, Product.all_columns())
    task['products'] = products

    return task


async def _get_tasks_list():
    tasks = await Task.select()
    return tasks


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
async def _change_task(id: int, params_to_update: dict):

    is_closed = params_to_update.get('is_closed', None)

    # Если статус закрытия партии меняется на True, то в closed_at необходимо выставить текущий datetime
    if is_closed is not None and is_closed:
        params_to_update['closed_at'] = datetime.now()

    # если наоборот -- то null
    if is_closed is not None and not is_closed:
        params_to_update['closed_at'] = None

    await Task.update(params_to_update).where(Task.id == id)

    task_updated = await _get_task_by_id(id=id)
    print(task_updated)

    return task_updated


async def _delete_task(id: int):
    task = await Task.delete().where(Task.id == id).returning(Task.id)
    return task

