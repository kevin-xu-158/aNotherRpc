# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo.proto',
  package='sogou.nlu.rpc.example',
  syntax='proto2',
  serialized_pb=_b('\n\necho.proto\x12\x15sogou.nlu.rpc.example\"\x1e\n\x0b\x45\x63hoRequest\x12\x0f\n\x07message\x18\x01 \x02(\t\"\x1f\n\x0c\x45\x63hoResponse\x12\x0f\n\x07message\x18\x01 \x02(\t2^\n\x0b\x45\x63hoService\x12O\n\x04\x65\x63ho\x12\".sogou.nlu.rpc.example.EchoRequest\x1a#.sogou.nlu.rpc.example.EchoResponseB\t\x80\x01\x01\x88\x01\x01\x90\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='sogou.nlu.rpc.example.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='sogou.nlu.rpc.example.EchoRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=67,
)


_ECHORESPONSE = _descriptor.Descriptor(
  name='EchoResponse',
  full_name='sogou.nlu.rpc.example.EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='sogou.nlu.rpc.example.EchoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), dict(
  DESCRIPTOR = _ECHOREQUEST,
  __module__ = 'echo_pb2'
  # @@protoc_insertion_point(class_scope:sogou.nlu.rpc.example.EchoRequest)
  ))
_sym_db.RegisterMessage(EchoRequest)

EchoResponse = _reflection.GeneratedProtocolMessageType('EchoResponse', (_message.Message,), dict(
  DESCRIPTOR = _ECHORESPONSE,
  __module__ = 'echo_pb2'
  # @@protoc_insertion_point(class_scope:sogou.nlu.rpc.example.EchoResponse)
  ))
_sym_db.RegisterMessage(EchoResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\200\001\001\210\001\001\220\001\001'))

_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='sogou.nlu.rpc.example.EchoService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=102,
  serialized_end=196,
  methods=[
  _descriptor.MethodDescriptor(
    name='echo',
    full_name='sogou.nlu.rpc.example.EchoService.echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHORESPONSE,
    options=None,
  ),
])

EchoService = service_reflection.GeneratedServiceType('EchoService', (_service.Service,), dict(
  DESCRIPTOR = _ECHOSERVICE,
  __module__ = 'echo_pb2'
  ))

EchoService_Stub = service_reflection.GeneratedServiceStubType('EchoService_Stub', (EchoService,), dict(
  DESCRIPTOR = _ECHOSERVICE,
  __module__ = 'echo_pb2'
  ))


# @@protoc_insertion_point(module_scope)
