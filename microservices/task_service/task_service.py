from grpc import aio
from protos import task_pb2_grpc, task_pb2
from microservices.task_service import db_tasks
from logs.logs import init_logger


logger = init_logger(__name__)


class TaskService(task_pb2_grpc.TaskServiceServicer):

    async def CreateTask(self, request, context):
        try:
            logger.info("CreateTask: request from api has received")
            product_created_id = await db_tasks._create_task(request_from_task_api=request)
            logger.info("CreateTask: task has been added")
            return task_pb2.CreateTaskResponse(id=product_created_id)
        except Exception as ex:
            logger.warning(f"CreateTask: task has not been added. Error: {str(ex)}")
            return task_pb2.CreateTaskResponse(id=None)

    async def GetTask(self, request, context):
        try:
            logger.info("GetTask: request from api has received")
            task = await db_tasks._get_task(id=request.id)
            logger.info("GetTask: task has been retrieved")
            return task_pb2.GetTaskResponse(task=task)
        except Exception as ex:
            logger.warning(f"CreateTask: task has not been retrieved from db. Error: {str(ex)}")
            return task_pb2.GetTaskResponse(task=None)

    async def GetTaskList(self, request, context):
        try:
            logger.info("GetTaskList: request from api has received")
            tasks = await db_tasks._get_tasks_list()
            return task_pb2.GetTaskListResponse(tasks=tasks)
        except Exception as ex:
            logger.warning(f"GetTaskList: tasks has not been retrieved from db. Error: {str(ex)}")
            return task_pb2.GetTaskListResponse(tasks=None)

    async def UpdateTask(self, request, context):

        try:
            logger.info("UpdateTask: request from api has received")
            task_updated_id = await db_tasks._change_task(params_to_update=request)
            logger.info("UpdateTask: task has been updated")
            return task_pb2.UpdateTaskResponse(id=task_updated_id)
        except Exception as ex:
            logger.warning(f"UpdateTask: task has not been updated. Error: {str(ex)}")
            return task_pb2.UpdateTaskResponse(id=None)

    async def DeleteTask(self, request, context):

        try:
            logger.info("DeleteTask: request from api has received")
            task_deleted_id = await db_tasks._delete_task(id=request.id)
            logger.info("DeleteTask: task has been deleted")
            return task_pb2.DeleteTaskResponse(id=task_deleted_id)
        except Exception as ex:
            logger.warning(f"DeleteTask: task has not been deleted. Error: {str(ex)}")
            return task_pb2.UpdateTaskResponse(id=None)


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
