# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_data_entry.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14get_data_entry.proto\x12\x08get_data\";\n\x13GetDataEntryRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x10\n\x08\x65ntry_id\x18\x02 \x01(\t\"7\n\x14GetDataEntryResponse\x12\x11\n\tdata_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2`\n\x0f\x44\x61taEntryGetter\x12M\n\x0cGetDataEntry\x12\x1d.get_data.GetDataEntryRequest\x1a\x1e.get_data.GetDataEntryResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_data_entry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETDATAENTRYREQUEST._serialized_start=34
  _GETDATAENTRYREQUEST._serialized_end=93
  _GETDATAENTRYRESPONSE._serialized_start=95
  _GETDATAENTRYRESPONSE._serialized_end=150
  _DATAENTRYGETTER._serialized_start=152
  _DATAENTRYGETTER._serialized_end=248
# @@protoc_insertion_point(module_scope)