from grpc import aio
from protos import task_pb2_grpc, task_pb2
from task import db_tasks


class TaskService(task_pb2_grpc.TaskServiceServicer):

    async def CreateTask(self, request, context):
        print("CreateTask")
        #print(request)
        res = await db_tasks._create_task(request_from_task_api=request)
        print(res)

        return task_pb2.CreateTaskResponse(id=1)

    async def GetTask(self, request, context):
        print("GetTask")
        task = await db_tasks._get_task(id=request.id)
        return task_pb2.GetTaskResponse(task=task)

    async def GetTaskList(self, request, context):
        print("GetTaskList")
        tasks = await db_tasks._get_tasks_list()
        return task_pb2.GetTaskListResponse(tasks=tasks)

    async def UpdateTask(self, request, context):
        print("UpdateTask")
        task = await db_tasks._change_task(params_to_update=request)
        task_updated_id = task[0]['id']
        return task_pb2.UpdateTaskResponse(id=task_updated_id)

    async def DeleteTask(self, request, context):

        task_deleted = await db_tasks._delete_task(id=request.id)
        print("DeleteTask")
        id = task_deleted[0]['id']
        return task_pb2.DeleteTaskResponse(id=id)


async def run_server(address):
    # Здесь получаем асинхронный сервер
    server = aio.server()
    print('START SERVER')
    # Регистрируем наш Todo сервер в aio сервере
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    # Теперь этот сервер необходимо зарегистрировать по какому-то адресу
    server.add_insecure_port(address)
    print('START SERVER')
    await server.start()
    await server.wait_for_termination()
