from google.protobuf import timestamp_pb2 as _timestamp_pb2
from protos import product_pb2 as _product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ("id", "is_closed", "closed_at", "task", "line", "shift", "group", "number_batch", "date_batch", "nomenclature", "code", "index", "date_begin", "date_end")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_CLOSED_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    NUMBER_BATCH_FIELD_NUMBER: _ClassVar[int]
    DATE_BATCH_FIELD_NUMBER: _ClassVar[int]
    NOMENCLATURE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DATE_BEGIN_FIELD_NUMBER: _ClassVar[int]
    DATE_END_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_closed: bool
    closed_at: _timestamp_pb2.Timestamp
    task: str
    line: str
    shift: str
    group: str
    number_batch: int
    date_batch: _timestamp_pb2.Timestamp
    nomenclature: str
    code: str
    index: str
    date_begin: _timestamp_pb2.Timestamp
    date_end: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., is_closed: bool = ..., closed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., task: _Optional[str] = ..., line: _Optional[str] = ..., shift: _Optional[str] = ..., group: _Optional[str] = ..., number_batch: _Optional[int] = ..., date_batch: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nomenclature: _Optional[str] = ..., code: _Optional[str] = ..., index: _Optional[str] = ..., date_begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateTaskRequest(_message.Message):
    __slots__ = ("is_closed", "closed_at", "task", "line", "shift", "group", "number_batch", "date_batch", "nomenclature", "code", "index", "date_begin", "date_end")
    IS_CLOSED_FIELD_NUMBER: _ClassVar[int]
    CLOSED_AT_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    NUMBER_BATCH_FIELD_NUMBER: _ClassVar[int]
    DATE_BATCH_FIELD_NUMBER: _ClassVar[int]
    NOMENCLATURE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DATE_BEGIN_FIELD_NUMBER: _ClassVar[int]
    DATE_END_FIELD_NUMBER: _ClassVar[int]
    is_closed: bool
    closed_at: _timestamp_pb2.Timestamp
    task: str
    line: str
    shift: str
    group: str
    number_batch: int
    date_batch: _timestamp_pb2.Timestamp
    nomenclature: str
    code: str
    index: str
    date_begin: _timestamp_pb2.Timestamp
    date_end: _timestamp_pb2.Timestamp
    def __init__(self, is_closed: bool = ..., closed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., task: _Optional[str] = ..., line: _Optional[str] = ..., shift: _Optional[str] = ..., group: _Optional[str] = ..., number_batch: _Optional[int] = ..., date_batch: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nomenclature: _Optional[str] = ..., code: _Optional[str] = ..., index: _Optional[str] = ..., date_begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateTaskResponse(_message.Message):
    __slots__ = ("task",)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: Task
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ...) -> None: ...

class GetTaskRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetTaskResponse(_message.Message):
    __slots__ = ("task", "products")
    TASK_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    task: Task
    products: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product]
    def __init__(self, task: _Optional[_Union[Task, _Mapping]] = ..., products: _Optional[_Iterable[_Union[_product_pb2.Product, _Mapping]]] = ...) -> None: ...

class GetTaskListRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetTaskListResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[Task]
    def __init__(self, tasks: _Optional[_Iterable[_Union[Task, _Mapping]]] = ...) -> None: ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteTaskResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
