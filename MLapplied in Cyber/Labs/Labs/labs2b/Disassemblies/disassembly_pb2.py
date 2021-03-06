# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: disassembly.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='disassembly.proto',
  package='targaryen',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x64isassembly.proto\x12\ttargaryen\"\xb1\x02\n\x11\x44isassemblyBinary\x12\x13\n\x0b\x62inary_name\x18\x01 \x01(\t\x12\x1a\n\x12\x62inary_sha256_hash\x18\x02 \x01(\x0c\x12=\n\x15\x64isassembly_func_list\x18\x03 \x03(\x0b\x32\x1e.targaryen.DisassemblyFunction\x12\x11\n\tproc_type\x18\x04 \x01(\r\x12\x11\n\tfile_type\x18\x05 \x01(\r\x12\x11\n\tword_size\x18\x06 \x01(\r\x12\x0f\n\x07\x65ndness\x18\x07 \x01(\r\x12\x15\n\rsegment_index\x18\x08 \x01(\r\x12\x16\n\x0etotal_segments\x18\t \x01(\r\x12\x33\n\x12import_symbol_list\x18\n \x03(\x0b\x32\x17.targaryen.ImportSymbol\"J\n\x0cImportSymbol\x12\x13\n\x0bimport_name\x18\x01 \x01(\t\x12\x14\n\x0clibrary_name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\x04\"\xac\x01\n\x13\x44isassemblyFunction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rstart_address\x18\x02 \x01(\x04\x12\x13\n\x0b\x65nd_address\x18\x03 \x01(\x04\x12\x14\n\x0csegment_name\x18\x04 \x01(\t\x12\x45\n\x1b\x64isassembly_basicblock_list\x18\x05 \x03(\x0b\x32 .targaryen.DisassemblyBasicBlock\"\x89\x01\n\x15\x44isassemblyBasicBlock\x12\x15\n\rstart_address\x18\x01 \x01(\x04\x12\x13\n\x0b\x65nd_address\x18\x02 \x01(\x04\x12\x44\n\x19\x64isassembly_instruct_list\x18\x03 \x03(\x0b\x32!.targaryen.DisassemblyInstruction\"Q\n\x16\x44isassemblyInstruction\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x04\x12\x14\n\x0copcode_bytes\x18\x02 \x01(\x0c\x12\x10\n\x08mnemonic\x18\x03 \x01(\tb\x06proto3')
)




_DISASSEMBLYBINARY = _descriptor.Descriptor(
  name='DisassemblyBinary',
  full_name='targaryen.DisassemblyBinary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary_name', full_name='targaryen.DisassemblyBinary.binary_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_sha256_hash', full_name='targaryen.DisassemblyBinary.binary_sha256_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disassembly_func_list', full_name='targaryen.DisassemblyBinary.disassembly_func_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proc_type', full_name='targaryen.DisassemblyBinary.proc_type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_type', full_name='targaryen.DisassemblyBinary.file_type', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='word_size', full_name='targaryen.DisassemblyBinary.word_size', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endness', full_name='targaryen.DisassemblyBinary.endness', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment_index', full_name='targaryen.DisassemblyBinary.segment_index', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_segments', full_name='targaryen.DisassemblyBinary.total_segments', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='import_symbol_list', full_name='targaryen.DisassemblyBinary.import_symbol_list', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=338,
)


_IMPORTSYMBOL = _descriptor.Descriptor(
  name='ImportSymbol',
  full_name='targaryen.ImportSymbol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='import_name', full_name='targaryen.ImportSymbol.import_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='library_name', full_name='targaryen.ImportSymbol.library_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='targaryen.ImportSymbol.address', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=414,
)


_DISASSEMBLYFUNCTION = _descriptor.Descriptor(
  name='DisassemblyFunction',
  full_name='targaryen.DisassemblyFunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='targaryen.DisassemblyFunction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_address', full_name='targaryen.DisassemblyFunction.start_address', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_address', full_name='targaryen.DisassemblyFunction.end_address', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment_name', full_name='targaryen.DisassemblyFunction.segment_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disassembly_basicblock_list', full_name='targaryen.DisassemblyFunction.disassembly_basicblock_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=589,
)


_DISASSEMBLYBASICBLOCK = _descriptor.Descriptor(
  name='DisassemblyBasicBlock',
  full_name='targaryen.DisassemblyBasicBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_address', full_name='targaryen.DisassemblyBasicBlock.start_address', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_address', full_name='targaryen.DisassemblyBasicBlock.end_address', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disassembly_instruct_list', full_name='targaryen.DisassemblyBasicBlock.disassembly_instruct_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=729,
)


_DISASSEMBLYINSTRUCTION = _descriptor.Descriptor(
  name='DisassemblyInstruction',
  full_name='targaryen.DisassemblyInstruction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='targaryen.DisassemblyInstruction.address', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opcode_bytes', full_name='targaryen.DisassemblyInstruction.opcode_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnemonic', full_name='targaryen.DisassemblyInstruction.mnemonic', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=731,
  serialized_end=812,
)

_DISASSEMBLYBINARY.fields_by_name['disassembly_func_list'].message_type = _DISASSEMBLYFUNCTION
_DISASSEMBLYBINARY.fields_by_name['import_symbol_list'].message_type = _IMPORTSYMBOL
_DISASSEMBLYFUNCTION.fields_by_name['disassembly_basicblock_list'].message_type = _DISASSEMBLYBASICBLOCK
_DISASSEMBLYBASICBLOCK.fields_by_name['disassembly_instruct_list'].message_type = _DISASSEMBLYINSTRUCTION
DESCRIPTOR.message_types_by_name['DisassemblyBinary'] = _DISASSEMBLYBINARY
DESCRIPTOR.message_types_by_name['ImportSymbol'] = _IMPORTSYMBOL
DESCRIPTOR.message_types_by_name['DisassemblyFunction'] = _DISASSEMBLYFUNCTION
DESCRIPTOR.message_types_by_name['DisassemblyBasicBlock'] = _DISASSEMBLYBASICBLOCK
DESCRIPTOR.message_types_by_name['DisassemblyInstruction'] = _DISASSEMBLYINSTRUCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisassemblyBinary = _reflection.GeneratedProtocolMessageType('DisassemblyBinary', (_message.Message,), dict(
  DESCRIPTOR = _DISASSEMBLYBINARY,
  __module__ = 'disassembly_pb2'
  # @@protoc_insertion_point(class_scope:targaryen.DisassemblyBinary)
  ))
_sym_db.RegisterMessage(DisassemblyBinary)

ImportSymbol = _reflection.GeneratedProtocolMessageType('ImportSymbol', (_message.Message,), dict(
  DESCRIPTOR = _IMPORTSYMBOL,
  __module__ = 'disassembly_pb2'
  # @@protoc_insertion_point(class_scope:targaryen.ImportSymbol)
  ))
_sym_db.RegisterMessage(ImportSymbol)

DisassemblyFunction = _reflection.GeneratedProtocolMessageType('DisassemblyFunction', (_message.Message,), dict(
  DESCRIPTOR = _DISASSEMBLYFUNCTION,
  __module__ = 'disassembly_pb2'
  # @@protoc_insertion_point(class_scope:targaryen.DisassemblyFunction)
  ))
_sym_db.RegisterMessage(DisassemblyFunction)

DisassemblyBasicBlock = _reflection.GeneratedProtocolMessageType('DisassemblyBasicBlock', (_message.Message,), dict(
  DESCRIPTOR = _DISASSEMBLYBASICBLOCK,
  __module__ = 'disassembly_pb2'
  # @@protoc_insertion_point(class_scope:targaryen.DisassemblyBasicBlock)
  ))
_sym_db.RegisterMessage(DisassemblyBasicBlock)

DisassemblyInstruction = _reflection.GeneratedProtocolMessageType('DisassemblyInstruction', (_message.Message,), dict(
  DESCRIPTOR = _DISASSEMBLYINSTRUCTION,
  __module__ = 'disassembly_pb2'
  # @@protoc_insertion_point(class_scope:targaryen.DisassemblyInstruction)
  ))
_sym_db.RegisterMessage(DisassemblyInstruction)


# @@protoc_insertion_point(module_scope)
