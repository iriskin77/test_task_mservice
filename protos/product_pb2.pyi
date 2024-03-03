from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("id", "unique_code", "number_batch", "is_aggregated", "aggregated_at", "date_product")
    ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CODE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_BATCH_FIELD_NUMBER: _ClassVar[int]
    IS_AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_AT_FIELD_NUMBER: _ClassVar[int]
    DATE_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    id: int
    unique_code: str
    number_batch: int
    is_aggregated: bool
    aggregated_at: float
    date_product: float
    def __init__(self, id: _Optional[int] = ..., unique_code: _Optional[str] = ..., number_batch: _Optional[int] = ..., is_aggregated: bool = ..., aggregated_at: _Optional[float] = ..., date_product: _Optional[float] = ...) -> None: ...

class ProductCreate(_message.Message):
    __slots__ = ("unique_code", "number_batch", "date_product")
    UNIQUE_CODE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_BATCH_FIELD_NUMBER: _ClassVar[int]
    DATE_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    unique_code: str
    number_batch: int
    date_product: float
    def __init__(self, unique_code: _Optional[str] = ..., number_batch: _Optional[int] = ..., date_product: _Optional[float] = ...) -> None: ...

class CreateProductRequest(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[ProductCreate]
    def __init__(self, products: _Optional[_Iterable[_Union[ProductCreate, _Mapping]]] = ...) -> None: ...

class CreateProductResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class GetProductsListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetProductsListResponse(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class AggregateRequest(_message.Message):
    __slots__ = ("unique_code",)
    UNIQUE_CODE_FIELD_NUMBER: _ClassVar[int]
    unique_code: str
    def __init__(self, unique_code: _Optional[str] = ...) -> None: ...

class AggregateResponse(_message.Message):
    __slots__ = ("is_aggregated",)
    IS_AGGREGATED_FIELD_NUMBER: _ClassVar[int]
    is_aggregated: bool
    def __init__(self, is_aggregated: bool = ...) -> None: ...
