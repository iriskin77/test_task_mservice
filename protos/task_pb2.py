# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/task.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import product_pb2 as protos_dot_product__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/task.proto\x12\x04task\x1a\x14protos/product.proto\"\xf5\x01\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tis_closed\x18\x02 \x01(\x08\x12\x11\n\tclosed_at\x18\x03 \x01(\x02\x12\x0c\n\x04task\x18\x04 \x01(\t\x12\x0c\n\x04line\x18\x05 \x01(\t\x12\r\n\x05shift\x18\x06 \x01(\t\x12\r\n\x05group\x18\x07 \x01(\t\x12\x14\n\x0cnumber_batch\x18\x08 \x01(\x04\x12\x12\n\ndate_batch\x18\t \x01(\x02\x12\x14\n\x0cnomenclature\x18\n \x01(\t\x12\x0c\n\x04\x63ode\x18\x0b \x01(\t\x12\r\n\x05index\x18\x0c \x01(\t\x12\x12\n\ndate_begin\x18\r \x01(\x02\x12\x10\n\x08\x64\x61te_end\x18\x0e \x01(\x02\"\xef\x01\n\nCreateTask\x12\x11\n\tis_closed\x18\x01 \x01(\x08\x12\x11\n\tclosed_at\x18\x02 \x01(\x02\x12\x0c\n\x04task\x18\x03 \x01(\t\x12\x0c\n\x04line\x18\x04 \x01(\t\x12\r\n\x05shift\x18\x05 \x01(\t\x12\r\n\x05group\x18\x06 \x01(\t\x12\x14\n\x0cnumber_batch\x18\x07 \x01(\x04\x12\x12\n\ndate_batch\x18\x08 \x01(\x02\x12\x14\n\x0cnomenclature\x18\t \x01(\t\x12\x0c\n\x04\x63ode\x18\n \x01(\t\x12\r\n\x05index\x18\x0b \x01(\t\x12\x12\n\ndate_begin\x18\x0c \x01(\x02\x12\x10\n\x08\x64\x61te_end\x18\r \x01(\x02\"\xf6\x01\n\x11\x43reateTaskRequest\x12\x11\n\tis_closed\x18\x01 \x01(\x08\x12\x11\n\tclosed_at\x18\x02 \x01(\x02\x12\x0c\n\x04task\x18\x03 \x01(\t\x12\x0c\n\x04line\x18\x04 \x01(\t\x12\r\n\x05shift\x18\x05 \x01(\t\x12\r\n\x05group\x18\x06 \x01(\t\x12\x14\n\x0cnumber_batch\x18\x07 \x01(\x04\x12\x12\n\ndate_batch\x18\x08 \x01(\x02\x12\x14\n\x0cnomenclature\x18\t \x01(\t\x12\x0c\n\x04\x63ode\x18\n \x01(\t\x12\r\n\x05index\x18\x0b \x01(\t\x12\x12\n\ndate_begin\x18\x0c \x01(\x02\x12\x10\n\x08\x64\x61te_end\x18\r \x01(\x02\" \n\x12\x43reateTaskResponse\x12\n\n\x02id\x18\x01 \x01(\x04\"\x1c\n\x0eGetTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"O\n\x0fGetTaskResponse\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.task.Task\x12\"\n\x08products\x18\x02 \x03(\x0b\x32\x10.product.Product\"\x14\n\x12GetTaskListRequest\"0\n\x13GetTaskListResponse\x12\x19\n\x05tasks\x18\x01 \x03(\x0b\x32\n.task.Task\"\xe5\x03\n\x11UpdateTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x16\n\tis_closed\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x16\n\tclosed_at\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04task\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04line\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x12\n\x05shift\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05group\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x19\n\x0cnumber_batch\x18\x08 \x01(\x04H\x06\x88\x01\x01\x12\x17\n\ndate_batch\x18\t \x01(\x02H\x07\x88\x01\x01\x12\x19\n\x0cnomenclature\x18\n \x01(\tH\x08\x88\x01\x01\x12\x11\n\x04\x63ode\x18\x0b \x01(\tH\t\x88\x01\x01\x12\x12\n\x05index\x18\x0c \x01(\tH\n\x88\x01\x01\x12\x17\n\ndate_begin\x18\r \x01(\x02H\x0b\x88\x01\x01\x12\x15\n\x08\x64\x61te_end\x18\x0e \x01(\x02H\x0c\x88\x01\x01\x42\x0c\n\n_is_closedB\x0c\n\n_closed_atB\x07\n\x05_taskB\x07\n\x05_lineB\x08\n\x06_shiftB\x08\n\x06_groupB\x0f\n\r_number_batchB\r\n\x0b_date_batchB\x0f\n\r_nomenclatureB\x07\n\x05_codeB\x08\n\x06_indexB\r\n\x0b_date_beginB\x0b\n\t_date_end\" \n\x12UpdateTaskResponse\x12\n\n\x02id\x18\x01 \x01(\x04\"\x1f\n\x11\x44\x65leteTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x04\" \n\x12\x44\x65leteTaskResponse\x12\n\n\x02id\x18\x01 \x01(\x04\x32\xcc\x02\n\x0bTaskService\x12?\n\nCreateTask\x12\x17.task.CreateTaskRequest\x1a\x18.task.CreateTaskResponse\x12\x36\n\x07GetTask\x12\x14.task.GetTaskRequest\x1a\x15.task.GetTaskResponse\x12\x42\n\x0bGetTaskList\x12\x18.task.GetTaskListRequest\x1a\x19.task.GetTaskListResponse\x12?\n\nUpdateTask\x12\x17.task.UpdateTaskRequest\x1a\x18.task.UpdateTaskResponse\x12?\n\nDeleteTask\x12\x17.task.DeleteTaskRequest\x1a\x18.task.DeleteTaskResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.task_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TASK']._serialized_start=50
  _globals['_TASK']._serialized_end=295
  _globals['_CREATETASK']._serialized_start=298
  _globals['_CREATETASK']._serialized_end=537
  _globals['_CREATETASKREQUEST']._serialized_start=540
  _globals['_CREATETASKREQUEST']._serialized_end=786
  _globals['_CREATETASKRESPONSE']._serialized_start=788
  _globals['_CREATETASKRESPONSE']._serialized_end=820
  _globals['_GETTASKREQUEST']._serialized_start=822
  _globals['_GETTASKREQUEST']._serialized_end=850
  _globals['_GETTASKRESPONSE']._serialized_start=852
  _globals['_GETTASKRESPONSE']._serialized_end=931
  _globals['_GETTASKLISTREQUEST']._serialized_start=933
  _globals['_GETTASKLISTREQUEST']._serialized_end=953
  _globals['_GETTASKLISTRESPONSE']._serialized_start=955
  _globals['_GETTASKLISTRESPONSE']._serialized_end=1003
  _globals['_UPDATETASKREQUEST']._serialized_start=1006
  _globals['_UPDATETASKREQUEST']._serialized_end=1491
  _globals['_UPDATETASKRESPONSE']._serialized_start=1493
  _globals['_UPDATETASKRESPONSE']._serialized_end=1525
  _globals['_DELETETASKREQUEST']._serialized_start=1527
  _globals['_DELETETASKREQUEST']._serialized_end=1558
  _globals['_DELETETASKRESPONSE']._serialized_start=1560
  _globals['_DELETETASKRESPONSE']._serialized_end=1592
  _globals['_TASKSERVICE']._serialized_start=1595
  _globals['_TASKSERVICE']._serialized_end=1927
# @@protoc_insertion_point(module_scope)
