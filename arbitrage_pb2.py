# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arbitrage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from messages import exchange_pb2 as messages_dot_exchange__pb2
from messages import trading_pair_pb2 as messages_dot_trading__pair__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arbitrage.proto',
  package='trading.arbitrage',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x61rbitrage.proto\x12\x11trading.arbitrage\x1a\x17messages/exchange.proto\x1a\x1bmessages/trading_pair.proto\"\x0e\n\x0c\x42\x61sicRequest\"\x0f\n\rBasicResponse\"\xec\x02\n\x11InitializeRequest\x12.\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x1f.trading.arbitrage.BasicRequest\x12\x33\n\x0f\x62uying_exchange\x18\x02 \x01(\x0b\x32\x1a.trading.messages.Exchange\x12\x34\n\x10selling_exchange\x18\x03 \x01(\x0b\x32\x1a.trading.messages.Exchange\x12\x33\n\x0ctrading_pair\x18\x04 \x01(\x0b\x32\x1d.trading.messages.TradingPair\x12\x35\n\x0c\x65nter_points\x18\x05 \x03(\x0b\x32\x1f.trading.arbitrage.TradingPoint\x12\x34\n\x0b\x65xit_points\x18\x06 \x03(\x0b\x32\x1f.trading.arbitrage.TradingPoint\x12\x1a\n\x12slippage_allowance\x18\x07 \x01(\x01\"r\n\x12InitializeResponse\x12/\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32 .trading.arbitrage.BasicResponse\x12+\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x1a.trading.arbitrage.Context\"\xe5\x01\n\x11HandleDataRequest\x12.\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x1f.trading.arbitrage.BasicRequest\x12+\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x1a.trading.arbitrage.Context\x12\x38\n\x0f\x62uying_exchange\x18\x03 \x01(\x0b\x32\x1f.trading.arbitrage.ExchangeData\x12\x39\n\x10selling_exchange\x18\x04 \x01(\x0b\x32\x1f.trading.arbitrage.ExchangeData\"r\n\x12HandleDataResponse\x12/\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32 .trading.arbitrage.BasicResponse\x12+\n\x07\x63ommand\x18\x02 \x01(\x0b\x32\x1a.trading.arbitrage.Command\"A\n\x0f\x41nalysisRequest\x12.\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32\x1f.trading.arbitrage.BasicRequest\"C\n\x10\x41nalysisResponse\x12/\n\x05\x62\x61sic\x18\x01 \x01(\x0b\x32 .trading.arbitrage.BasicResponse\"\xb2\x02\n\x07\x43ontext\x12\x33\n\x0f\x62uying_exchange\x18\x01 \x01(\x0b\x32\x1a.trading.messages.Exchange\x12\x34\n\x10selling_exchange\x18\x02 \x01(\x0b\x32\x1a.trading.messages.Exchange\x12\x33\n\x0ctrading_pair\x18\x03 \x01(\x0b\x32\x1d.trading.messages.TradingPair\x12\x35\n\x0c\x65ntry_points\x18\x04 \x03(\x0b\x32\x1f.trading.arbitrage.TradingPoint\x12\x34\n\x0b\x65xit_points\x18\x05 \x03(\x0b\x32\x1f.trading.arbitrage.TradingPoint\x12\x1a\n\x12slippage_allowance\x18\x06 \x01(\x01\"+\n\x0cTradingPoint\x12\x0b\n\x03gap\x18\x01 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\"F\n\x0c\x45xchangeData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1a.trading.arbitrage.BarData\"Q\n\x07\x42\x61rData\x12\x0c\n\x04open\x18\x01 \x01(\x01\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\x0e\n\x06volume\x18\x05 \x01(\x01\"\xa2\x01\n\x07\x43ommand\x12\x31\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32!.trading.arbitrage.Command.Action\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x12\x14\n\x0c\x62uying_price\x18\x03 \x01(\x01\x12\x15\n\rselling_price\x18\x04 \x01(\x01\"\'\n\x06\x41\x63tion\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45NTER\x10\x01\x12\x08\n\x04\x45XIT\x10\x02\x32\x9d\x02\n\x10\x41rbitrageService\x12Y\n\nInitialize\x12$.trading.arbitrage.InitializeRequest\x1a%.trading.arbitrage.InitializeResponse\x12Y\n\nHandleData\x12$.trading.arbitrage.HandleDataRequest\x1a%.trading.arbitrage.HandleDataResponse\x12S\n\x08\x41nalysis\x12\".trading.arbitrage.AnalysisRequest\x1a#.trading.arbitrage.AnalysisResponseb\x06proto3')
  ,
  dependencies=[messages_dot_exchange__pb2.DESCRIPTOR,messages_dot_trading__pair__pb2.DESCRIPTOR,])



_COMMAND_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='trading.arbitrage.Command.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1725,
  serialized_end=1764,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_ACTION)


_BASICREQUEST = _descriptor.Descriptor(
  name='BasicRequest',
  full_name='trading.arbitrage.BasicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=92,
  serialized_end=106,
)


_BASICRESPONSE = _descriptor.Descriptor(
  name='BasicResponse',
  full_name='trading.arbitrage.BasicResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=108,
  serialized_end=123,
)


_INITIALIZEREQUEST = _descriptor.Descriptor(
  name='InitializeRequest',
  full_name='trading.arbitrage.InitializeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='trading.arbitrage.InitializeRequest.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buying_exchange', full_name='trading.arbitrage.InitializeRequest.buying_exchange', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selling_exchange', full_name='trading.arbitrage.InitializeRequest.selling_exchange', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading_pair', full_name='trading.arbitrage.InitializeRequest.trading_pair', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enter_points', full_name='trading.arbitrage.InitializeRequest.enter_points', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_points', full_name='trading.arbitrage.InitializeRequest.exit_points', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slippage_allowance', full_name='trading.arbitrage.InitializeRequest.slippage_allowance', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=126,
  serialized_end=490,
)


_INITIALIZERESPONSE = _descriptor.Descriptor(
  name='InitializeResponse',
  full_name='trading.arbitrage.InitializeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='trading.arbitrage.InitializeResponse.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='trading.arbitrage.InitializeResponse.context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=492,
  serialized_end=606,
)


_HANDLEDATAREQUEST = _descriptor.Descriptor(
  name='HandleDataRequest',
  full_name='trading.arbitrage.HandleDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='trading.arbitrage.HandleDataRequest.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='trading.arbitrage.HandleDataRequest.context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buying_exchange', full_name='trading.arbitrage.HandleDataRequest.buying_exchange', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selling_exchange', full_name='trading.arbitrage.HandleDataRequest.selling_exchange', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=609,
  serialized_end=838,
)


_HANDLEDATARESPONSE = _descriptor.Descriptor(
  name='HandleDataResponse',
  full_name='trading.arbitrage.HandleDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='trading.arbitrage.HandleDataResponse.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='trading.arbitrage.HandleDataResponse.command', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=840,
  serialized_end=954,
)


_ANALYSISREQUEST = _descriptor.Descriptor(
  name='AnalysisRequest',
  full_name='trading.arbitrage.AnalysisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='trading.arbitrage.AnalysisRequest.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=956,
  serialized_end=1021,
)


_ANALYSISRESPONSE = _descriptor.Descriptor(
  name='AnalysisResponse',
  full_name='trading.arbitrage.AnalysisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic', full_name='trading.arbitrage.AnalysisResponse.basic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1023,
  serialized_end=1090,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='trading.arbitrage.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buying_exchange', full_name='trading.arbitrage.Context.buying_exchange', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selling_exchange', full_name='trading.arbitrage.Context.selling_exchange', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading_pair', full_name='trading.arbitrage.Context.trading_pair', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entry_points', full_name='trading.arbitrage.Context.entry_points', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_points', full_name='trading.arbitrage.Context.exit_points', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slippage_allowance', full_name='trading.arbitrage.Context.slippage_allowance', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1093,
  serialized_end=1399,
)


_TRADINGPOINT = _descriptor.Descriptor(
  name='TradingPoint',
  full_name='trading.arbitrage.TradingPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gap', full_name='trading.arbitrage.TradingPoint.gap', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='trading.arbitrage.TradingPoint.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1401,
  serialized_end=1444,
)


_EXCHANGEDATA = _descriptor.Descriptor(
  name='ExchangeData',
  full_name='trading.arbitrage.ExchangeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='trading.arbitrage.ExchangeData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='trading.arbitrage.ExchangeData.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1446,
  serialized_end=1516,
)


_BARDATA = _descriptor.Descriptor(
  name='BarData',
  full_name='trading.arbitrage.BarData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open', full_name='trading.arbitrage.BarData.open', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='trading.arbitrage.BarData.close', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='trading.arbitrage.BarData.high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='trading.arbitrage.BarData.low', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='trading.arbitrage.BarData.volume', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1518,
  serialized_end=1599,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='trading.arbitrage.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='trading.arbitrage.Command.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='trading.arbitrage.Command.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buying_price', full_name='trading.arbitrage.Command.buying_price', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selling_price', full_name='trading.arbitrage.Command.selling_price', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMAND_ACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1602,
  serialized_end=1764,
)

_INITIALIZEREQUEST.fields_by_name['basic'].message_type = _BASICREQUEST
_INITIALIZEREQUEST.fields_by_name['buying_exchange'].message_type = messages_dot_exchange__pb2._EXCHANGE
_INITIALIZEREQUEST.fields_by_name['selling_exchange'].message_type = messages_dot_exchange__pb2._EXCHANGE
_INITIALIZEREQUEST.fields_by_name['trading_pair'].message_type = messages_dot_trading__pair__pb2._TRADINGPAIR
_INITIALIZEREQUEST.fields_by_name['enter_points'].message_type = _TRADINGPOINT
_INITIALIZEREQUEST.fields_by_name['exit_points'].message_type = _TRADINGPOINT
_INITIALIZERESPONSE.fields_by_name['basic'].message_type = _BASICRESPONSE
_INITIALIZERESPONSE.fields_by_name['context'].message_type = _CONTEXT
_HANDLEDATAREQUEST.fields_by_name['basic'].message_type = _BASICREQUEST
_HANDLEDATAREQUEST.fields_by_name['context'].message_type = _CONTEXT
_HANDLEDATAREQUEST.fields_by_name['buying_exchange'].message_type = _EXCHANGEDATA
_HANDLEDATAREQUEST.fields_by_name['selling_exchange'].message_type = _EXCHANGEDATA
_HANDLEDATARESPONSE.fields_by_name['basic'].message_type = _BASICRESPONSE
_HANDLEDATARESPONSE.fields_by_name['command'].message_type = _COMMAND
_ANALYSISREQUEST.fields_by_name['basic'].message_type = _BASICREQUEST
_ANALYSISRESPONSE.fields_by_name['basic'].message_type = _BASICRESPONSE
_CONTEXT.fields_by_name['buying_exchange'].message_type = messages_dot_exchange__pb2._EXCHANGE
_CONTEXT.fields_by_name['selling_exchange'].message_type = messages_dot_exchange__pb2._EXCHANGE
_CONTEXT.fields_by_name['trading_pair'].message_type = messages_dot_trading__pair__pb2._TRADINGPAIR
_CONTEXT.fields_by_name['entry_points'].message_type = _TRADINGPOINT
_CONTEXT.fields_by_name['exit_points'].message_type = _TRADINGPOINT
_EXCHANGEDATA.fields_by_name['data'].message_type = _BARDATA
_COMMAND.fields_by_name['action'].enum_type = _COMMAND_ACTION
_COMMAND_ACTION.containing_type = _COMMAND
DESCRIPTOR.message_types_by_name['BasicRequest'] = _BASICREQUEST
DESCRIPTOR.message_types_by_name['BasicResponse'] = _BASICRESPONSE
DESCRIPTOR.message_types_by_name['InitializeRequest'] = _INITIALIZEREQUEST
DESCRIPTOR.message_types_by_name['InitializeResponse'] = _INITIALIZERESPONSE
DESCRIPTOR.message_types_by_name['HandleDataRequest'] = _HANDLEDATAREQUEST
DESCRIPTOR.message_types_by_name['HandleDataResponse'] = _HANDLEDATARESPONSE
DESCRIPTOR.message_types_by_name['AnalysisRequest'] = _ANALYSISREQUEST
DESCRIPTOR.message_types_by_name['AnalysisResponse'] = _ANALYSISRESPONSE
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['TradingPoint'] = _TRADINGPOINT
DESCRIPTOR.message_types_by_name['ExchangeData'] = _EXCHANGEDATA
DESCRIPTOR.message_types_by_name['BarData'] = _BARDATA
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BasicRequest = _reflection.GeneratedProtocolMessageType('BasicRequest', (_message.Message,), dict(
  DESCRIPTOR = _BASICREQUEST,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.BasicRequest)
  ))
_sym_db.RegisterMessage(BasicRequest)

BasicResponse = _reflection.GeneratedProtocolMessageType('BasicResponse', (_message.Message,), dict(
  DESCRIPTOR = _BASICRESPONSE,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.BasicResponse)
  ))
_sym_db.RegisterMessage(BasicResponse)

InitializeRequest = _reflection.GeneratedProtocolMessageType('InitializeRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZEREQUEST,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.InitializeRequest)
  ))
_sym_db.RegisterMessage(InitializeRequest)

InitializeResponse = _reflection.GeneratedProtocolMessageType('InitializeResponse', (_message.Message,), dict(
  DESCRIPTOR = _INITIALIZERESPONSE,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.InitializeResponse)
  ))
_sym_db.RegisterMessage(InitializeResponse)

HandleDataRequest = _reflection.GeneratedProtocolMessageType('HandleDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _HANDLEDATAREQUEST,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.HandleDataRequest)
  ))
_sym_db.RegisterMessage(HandleDataRequest)

HandleDataResponse = _reflection.GeneratedProtocolMessageType('HandleDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _HANDLEDATARESPONSE,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.HandleDataResponse)
  ))
_sym_db.RegisterMessage(HandleDataResponse)

AnalysisRequest = _reflection.GeneratedProtocolMessageType('AnalysisRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISREQUEST,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.AnalysisRequest)
  ))
_sym_db.RegisterMessage(AnalysisRequest)

AnalysisResponse = _reflection.GeneratedProtocolMessageType('AnalysisResponse', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISRESPONSE,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.AnalysisResponse)
  ))
_sym_db.RegisterMessage(AnalysisResponse)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.Context)
  ))
_sym_db.RegisterMessage(Context)

TradingPoint = _reflection.GeneratedProtocolMessageType('TradingPoint', (_message.Message,), dict(
  DESCRIPTOR = _TRADINGPOINT,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.TradingPoint)
  ))
_sym_db.RegisterMessage(TradingPoint)

ExchangeData = _reflection.GeneratedProtocolMessageType('ExchangeData', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEDATA,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.ExchangeData)
  ))
_sym_db.RegisterMessage(ExchangeData)

BarData = _reflection.GeneratedProtocolMessageType('BarData', (_message.Message,), dict(
  DESCRIPTOR = _BARDATA,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.BarData)
  ))
_sym_db.RegisterMessage(BarData)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'arbitrage_pb2'
  # @@protoc_insertion_point(class_scope:trading.arbitrage.Command)
  ))
_sym_db.RegisterMessage(Command)



_ARBITRAGESERVICE = _descriptor.ServiceDescriptor(
  name='ArbitrageService',
  full_name='trading.arbitrage.ArbitrageService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1767,
  serialized_end=2052,
  methods=[
  _descriptor.MethodDescriptor(
    name='Initialize',
    full_name='trading.arbitrage.ArbitrageService.Initialize',
    index=0,
    containing_service=None,
    input_type=_INITIALIZEREQUEST,
    output_type=_INITIALIZERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HandleData',
    full_name='trading.arbitrage.ArbitrageService.HandleData',
    index=1,
    containing_service=None,
    input_type=_HANDLEDATAREQUEST,
    output_type=_HANDLEDATARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Analysis',
    full_name='trading.arbitrage.ArbitrageService.Analysis',
    index=2,
    containing_service=None,
    input_type=_ANALYSISREQUEST,
    output_type=_ANALYSISRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARBITRAGESERVICE)

DESCRIPTOR.services_by_name['ArbitrageService'] = _ARBITRAGESERVICE

# @@protoc_insertion_point(module_scope)
