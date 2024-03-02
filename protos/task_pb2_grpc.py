# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import task_pb2 as protos_dot_task__pb2


class TaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTask = channel.unary_unary(
                '/task.TaskService/CreateTask',
                request_serializer=protos_dot_task__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=protos_dot_task__pb2.CreateTaskResponse.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/task.TaskService/GetTask',
                request_serializer=protos_dot_task__pb2.GetTaskRequest.SerializeToString,
                response_deserializer=protos_dot_task__pb2.GetTaskResponse.FromString,
                )
        self.GetTaskList = channel.unary_unary(
                '/task.TaskService/GetTaskList',
                request_serializer=protos_dot_task__pb2.GetTaskListRequest.SerializeToString,
                response_deserializer=protos_dot_task__pb2.GetTaskListResponse.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/task.TaskService/UpdateTask',
                request_serializer=protos_dot_task__pb2.UpdateTaskRequest.SerializeToString,
                response_deserializer=protos_dot_task__pb2.UpdateTaskResponse.FromString,
                )
        self.DeleteTask = channel.unary_unary(
                '/task.TaskService/DeleteTask',
                request_serializer=protos_dot_task__pb2.DeleteTaskRequest.SerializeToString,
                response_deserializer=protos_dot_task__pb2.DeleteTaskResponse.FromString,
                )


class TaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=protos_dot_task__pb2.CreateTaskRequest.FromString,
                    response_serializer=protos_dot_task__pb2.CreateTaskResponse.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=protos_dot_task__pb2.GetTaskRequest.FromString,
                    response_serializer=protos_dot_task__pb2.GetTaskResponse.SerializeToString,
            ),
            'GetTaskList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskList,
                    request_deserializer=protos_dot_task__pb2.GetTaskListRequest.FromString,
                    response_serializer=protos_dot_task__pb2.GetTaskListResponse.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=protos_dot_task__pb2.UpdateTaskRequest.FromString,
                    response_serializer=protos_dot_task__pb2.UpdateTaskResponse.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=protos_dot_task__pb2.DeleteTaskRequest.FromString,
                    response_serializer=protos_dot_task__pb2.DeleteTaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'task.TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/CreateTask',
            protos_dot_task__pb2.CreateTaskRequest.SerializeToString,
            protos_dot_task__pb2.CreateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/GetTask',
            protos_dot_task__pb2.GetTaskRequest.SerializeToString,
            protos_dot_task__pb2.GetTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/GetTaskList',
            protos_dot_task__pb2.GetTaskListRequest.SerializeToString,
            protos_dot_task__pb2.GetTaskListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/UpdateTask',
            protos_dot_task__pb2.UpdateTaskRequest.SerializeToString,
            protos_dot_task__pb2.UpdateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/DeleteTask',
            protos_dot_task__pb2.DeleteTaskRequest.SerializeToString,
            protos_dot_task__pb2.DeleteTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
