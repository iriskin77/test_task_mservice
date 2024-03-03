from protos import product_pb2 as _product_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductToAggregateRequest(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class ProductToAggregateResponse(_message.Message):
    __slots__ = ("is_aggregated",)
    IS_AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    is_aggregated: bool
    def __init__(self, is_aggregated: bool = ...) -> None: ...
