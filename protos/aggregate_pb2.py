# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/aggregate.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16protos/aggregate.proto\x12\taggregate\x1a\x1egoogle/protobuf/wrappers.proto\"0\n\x19ProductToAggregateRequest\x12\x13\n\x0bunique_code\x18\x01 \x01(\t\"_\n\x1aProductToAggregateResponse\x12\x13\n\x0bunique_code\x18\x01 \x01(\t\x12\x15\n\ris_aggregated\x18\x02 \x01(\x08\x12\x15\n\raggregated_at\x18\x03 \x01(\x02\"6\n\x1fStatusProductAggregationRequest\x12\x13\n\x0bunique_code\x18\x01 \x01(\t\"9\n StatusProductAggregationResponse\x12\x15\n\ris_aggregated\x18\x01 \x01(\x08\x32\xd5\x01\n\x12\x41ggregationService\x12_\n\x10\x41ggregateProduct\x12$.aggregate.ProductToAggregateRequest\x1a%.aggregate.ProductToAggregateResponse\x12^\n\x14GetStatusAggregation\x12*.aggregate.StatusProductAggregationRequest\x1a\x1a.google.protobuf.BoolValueb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.aggregate_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PRODUCTTOAGGREGATEREQUEST']._serialized_start=69
  _globals['_PRODUCTTOAGGREGATEREQUEST']._serialized_end=117
  _globals['_PRODUCTTOAGGREGATERESPONSE']._serialized_start=119
  _globals['_PRODUCTTOAGGREGATERESPONSE']._serialized_end=214
  _globals['_STATUSPRODUCTAGGREGATIONREQUEST']._serialized_start=216
  _globals['_STATUSPRODUCTAGGREGATIONREQUEST']._serialized_end=270
  _globals['_STATUSPRODUCTAGGREGATIONRESPONSE']._serialized_start=272
  _globals['_STATUSPRODUCTAGGREGATIONRESPONSE']._serialized_end=329
  _globals['_AGGREGATIONSERVICE']._serialized_start=332
  _globals['_AGGREGATIONSERVICE']._serialized_end=545
# @@protoc_insertion_point(module_scope)
