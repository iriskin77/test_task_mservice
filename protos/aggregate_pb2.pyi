from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProductToAggregateRequest(_message.Message):
    __slots__ = ("unique_code",)
    UNIQUE_CODE_FIELD_NUMBER: _ClassVar[int]
    unique_code: str
    def __init__(self, unique_code: _Optional[str] = ...) -> None: ...

class ProductToAggregateResponse(_message.Message):
    __slots__ = ("unique_code", "is_aggregated", "aggregated_at")
    UNIQUE_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_AT_FIELD_NUMBER: _ClassVar[int]
    unique_code: str
    is_aggregated: bool
    aggregated_at: float
    def __init__(self, unique_code: _Optional[str] = ..., is_aggregated: bool = ..., aggregated_at: _Optional[float] = ...) -> None: ...

class StatusProductAggregationRequest(_message.Message):
    __slots__ = ("unique_code",)
    UNIQUE_CODE_FIELD_NUMBER: _ClassVar[int]
    unique_code: str
    def __init__(self, unique_code: _Optional[str] = ...) -> None: ...

class StatusProductAggregationResponse(_message.Message):
    __slots__ = ("is_aggregated",)
    IS_AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    is_aggregated: bool
    def __init__(self, is_aggregated: bool = ...) -> None: ...
