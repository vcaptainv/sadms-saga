# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"0\n\nAddRequest\x12\x10\n\x08operand1\x18\x01 \x01(\x05\x12\x10\n\x08operand2\x18\x02 \x01(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\"5\n\x0fMultiplyRequest\x12\x10\n\x08operand1\x18\x01 \x01(\x05\x12\x10\n\x08operand2\x18\x02 \x01(\x05\"\"\n\x10MultiplyResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\x8f\x01\n\nCalculator\x12\x38\n\x03\x41\x64\x64\x12\x16.calculator.AddRequest\x1a\x17.calculator.AddResponse\"\x00\x12G\n\x08Multiply\x12\x1b.calculator.MultiplyRequest\x1a\x1c.calculator.MultiplyResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=32
  _ADDREQUEST._serialized_end=80
  _ADDRESPONSE._serialized_start=82
  _ADDRESPONSE._serialized_end=111
  _MULTIPLYREQUEST._serialized_start=113
  _MULTIPLYREQUEST._serialized_end=166
  _MULTIPLYRESPONSE._serialized_start=168
  _MULTIPLYRESPONSE._serialized_end=202
  _CALCULATOR._serialized_start=205
  _CALCULATOR._serialized_end=348
# @@protoc_insertion_point(module_scope)
