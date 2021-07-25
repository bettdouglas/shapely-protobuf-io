# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: earth_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='earth_service.proto',
  package='countries',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x65\x61rth_service.proto\x12\tcountries\x1a\x0egeometry.proto\"P\n\x07\x43ountry\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x08geometry\x18\x03 \x01(\x0b\x32\t.Geometry\x12\x0c\n\x04type\x18\x04 \x01(\t\"2\n\tCountries\x12%\n\tcountries\x18\x01 \x03(\x0b\x32\x12.countries.Country\")\n\x16GetAllCountriesRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"<\n\x1dGetCountriesInBoundaryRequest\x12\x1b\n\x08\x62oundary\x18\x01 \x01(\x0b\x32\t.Geometry\")\n\x16SearchCountriesRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t2\x80\x02\n\x0c\x45\x61rthService\x12J\n\x0fGetAllCountries\x12!.countries.GetAllCountriesRequest\x1a\x14.countries.Countries\x12J\n\x0fSearchCountries\x12!.countries.SearchCountriesRequest\x1a\x14.countries.Countries\x12X\n\x16GetCountriesInBoundary\x12(.countries.GetCountriesInBoundaryRequest\x1a\x14.countries.Countriesb\x06proto3'
  ,
  dependencies=[geometry__pb2.DESCRIPTOR,])




_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='countries.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='countries.Country.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='countries.Country.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='countries.Country.geometry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='countries.Country.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=130,
)


_COUNTRIES = _descriptor.Descriptor(
  name='Countries',
  full_name='countries.Countries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='countries', full_name='countries.Countries.countries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=182,
)


_GETALLCOUNTRIESREQUEST = _descriptor.Descriptor(
  name='GetAllCountriesRequest',
  full_name='countries.GetAllCountriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='countries.GetAllCountriesRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=225,
)


_GETCOUNTRIESINBOUNDARYREQUEST = _descriptor.Descriptor(
  name='GetCountriesInBoundaryRequest',
  full_name='countries.GetCountriesInBoundaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='boundary', full_name='countries.GetCountriesInBoundaryRequest.boundary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=287,
)


_SEARCHCOUNTRIESREQUEST = _descriptor.Descriptor(
  name='SearchCountriesRequest',
  full_name='countries.SearchCountriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword', full_name='countries.SearchCountriesRequest.keyword', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=330,
)

_COUNTRY.fields_by_name['geometry'].message_type = geometry__pb2._GEOMETRY
_COUNTRIES.fields_by_name['countries'].message_type = _COUNTRY
_GETCOUNTRIESINBOUNDARYREQUEST.fields_by_name['boundary'].message_type = geometry__pb2._GEOMETRY
DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
DESCRIPTOR.message_types_by_name['Countries'] = _COUNTRIES
DESCRIPTOR.message_types_by_name['GetAllCountriesRequest'] = _GETALLCOUNTRIESREQUEST
DESCRIPTOR.message_types_by_name['GetCountriesInBoundaryRequest'] = _GETCOUNTRIESINBOUNDARYREQUEST
DESCRIPTOR.message_types_by_name['SearchCountriesRequest'] = _SEARCHCOUNTRIESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRY,
  '__module__' : 'earth_service_pb2'
  # @@protoc_insertion_point(class_scope:countries.Country)
  })
_sym_db.RegisterMessage(Country)

Countries = _reflection.GeneratedProtocolMessageType('Countries', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRIES,
  '__module__' : 'earth_service_pb2'
  # @@protoc_insertion_point(class_scope:countries.Countries)
  })
_sym_db.RegisterMessage(Countries)

GetAllCountriesRequest = _reflection.GeneratedProtocolMessageType('GetAllCountriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLCOUNTRIESREQUEST,
  '__module__' : 'earth_service_pb2'
  # @@protoc_insertion_point(class_scope:countries.GetAllCountriesRequest)
  })
_sym_db.RegisterMessage(GetAllCountriesRequest)

GetCountriesInBoundaryRequest = _reflection.GeneratedProtocolMessageType('GetCountriesInBoundaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOUNTRIESINBOUNDARYREQUEST,
  '__module__' : 'earth_service_pb2'
  # @@protoc_insertion_point(class_scope:countries.GetCountriesInBoundaryRequest)
  })
_sym_db.RegisterMessage(GetCountriesInBoundaryRequest)

SearchCountriesRequest = _reflection.GeneratedProtocolMessageType('SearchCountriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCOUNTRIESREQUEST,
  '__module__' : 'earth_service_pb2'
  # @@protoc_insertion_point(class_scope:countries.SearchCountriesRequest)
  })
_sym_db.RegisterMessage(SearchCountriesRequest)



_EARTHSERVICE = _descriptor.ServiceDescriptor(
  name='EarthService',
  full_name='countries.EarthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=333,
  serialized_end=589,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllCountries',
    full_name='countries.EarthService.GetAllCountries',
    index=0,
    containing_service=None,
    input_type=_GETALLCOUNTRIESREQUEST,
    output_type=_COUNTRIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchCountries',
    full_name='countries.EarthService.SearchCountries',
    index=1,
    containing_service=None,
    input_type=_SEARCHCOUNTRIESREQUEST,
    output_type=_COUNTRIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCountriesInBoundary',
    full_name='countries.EarthService.GetCountriesInBoundary',
    index=2,
    containing_service=None,
    input_type=_GETCOUNTRIESINBOUNDARYREQUEST,
    output_type=_COUNTRIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EARTHSERVICE)

DESCRIPTOR.services_by_name['EarthService'] = _EARTHSERVICE

# @@protoc_insertion_point(module_scope)
