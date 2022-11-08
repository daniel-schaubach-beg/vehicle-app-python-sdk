"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _NullValue:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _NullValueEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NullValue.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NULL_VALUE_UNSPECIFIED: _NullValue.ValueType  # 0
class NullValue(_NullValue, metaclass=_NullValueEnumTypeWrapper):
    pass

NULL_VALUE_UNSPECIFIED: NullValue.ValueType  # 0
global___NullValue = NullValue


class Intent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISCOVER_FIELD_NUMBER: builtins.int
    INVOKE_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    WRITE_FIELD_NUMBER: builtins.int
    INSPECT_FIELD_NUMBER: builtins.int
    SUBSCRIBE_FIELD_NUMBER: builtins.int
    @property
    def discover(self) -> global___DiscoverIntent: ...
    @property
    def invoke(self) -> global___InvokeIntent: ...
    @property
    def read(self) -> global___ReadIntent: ...
    @property
    def write(self) -> global___WriteIntent: ...
    @property
    def inspect(self) -> global___InspectIntent: ...
    @property
    def subscribe(self) -> global___SubscribeIntent: ...
    def __init__(self,
        *,
        discover: typing.Optional[global___DiscoverIntent] = ...,
        invoke: typing.Optional[global___InvokeIntent] = ...,
        read: typing.Optional[global___ReadIntent] = ...,
        write: typing.Optional[global___WriteIntent] = ...,
        inspect: typing.Optional[global___InspectIntent] = ...,
        subscribe: typing.Optional[global___SubscribeIntent] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["discover",b"discover","inspect",b"inspect","intent",b"intent","invoke",b"invoke","read",b"read","subscribe",b"subscribe","write",b"write"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["discover",b"discover","inspect",b"inspect","intent",b"intent","invoke",b"invoke","read",b"read","subscribe",b"subscribe","write",b"write"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["intent",b"intent"]) -> typing.Optional[typing_extensions.Literal["discover","invoke","read","write","inspect","subscribe"]]: ...
global___Intent = Intent

class ReadIntent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    key: typing.Text
    def __init__(self,
        *,
        key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___ReadIntent = ReadIntent

class ReadFulfillment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> global___Value: ...
    def __init__(self,
        *,
        value: typing.Optional[global___Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___ReadFulfillment = ReadFulfillment

class WriteIntent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: typing.Text
    @property
    def value(self) -> global___Value: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        value: typing.Optional[global___Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...
global___WriteIntent = WriteIntent

class WriteFulfillment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___WriteFulfillment = WriteFulfillment

class SubscribeIntent(google.protobuf.message.Message):
    """* Subscribe to a source on the application. This requires an already open streaming channel.
    The `channel_id` is used to identify the channel to use for subscription. This is provided
    by the provider as a gRPC metadata header when establishing a channel through the streaming
    interface call. See [chariott.streaming.v1.proto](chariott.streaming.v1.proto) for more details.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    SOURCES_FIELD_NUMBER: builtins.int
    channel_id: typing.Text
    @property
    def sources(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        channel_id: typing.Text = ...,
        sources: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["channel_id",b"channel_id","sources",b"sources"]) -> None: ...
global___SubscribeIntent = SubscribeIntent

class SubscribeFulfillment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___SubscribeFulfillment = SubscribeFulfillment

class Fulfillment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DISCOVER_FIELD_NUMBER: builtins.int
    INSPECT_FIELD_NUMBER: builtins.int
    READ_FIELD_NUMBER: builtins.int
    WRITE_FIELD_NUMBER: builtins.int
    INVOKE_FIELD_NUMBER: builtins.int
    SUBSCRIBE_FIELD_NUMBER: builtins.int
    @property
    def discover(self) -> global___DiscoverFulfillment: ...
    @property
    def inspect(self) -> global___InspectFulfillment: ...
    @property
    def read(self) -> global___ReadFulfillment: ...
    @property
    def write(self) -> global___WriteFulfillment: ...
    @property
    def invoke(self) -> global___InvokeFulfillment: ...
    @property
    def subscribe(self) -> global___SubscribeFulfillment: ...
    def __init__(self,
        *,
        discover: typing.Optional[global___DiscoverFulfillment] = ...,
        inspect: typing.Optional[global___InspectFulfillment] = ...,
        read: typing.Optional[global___ReadFulfillment] = ...,
        write: typing.Optional[global___WriteFulfillment] = ...,
        invoke: typing.Optional[global___InvokeFulfillment] = ...,
        subscribe: typing.Optional[global___SubscribeFulfillment] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["discover",b"discover","fulfillment",b"fulfillment","inspect",b"inspect","invoke",b"invoke","read",b"read","subscribe",b"subscribe","write",b"write"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["discover",b"discover","fulfillment",b"fulfillment","inspect",b"inspect","invoke",b"invoke","read",b"read","subscribe",b"subscribe","write",b"write"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["fulfillment",b"fulfillment"]) -> typing.Optional[typing_extensions.Literal["discover","inspect","read","write","invoke","subscribe"]]: ...
global___Fulfillment = Fulfillment

class DiscoverIntent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DiscoverIntent = DiscoverIntent

class DiscoverFulfillment(google.protobuf.message.Message):
    """*
    Discover Fulfillment

    Returns a list of services that are provided by the application with their corresponding url endpoint, schema type and reference.
    The `schema_kind` is defining the contract depending of the `schema_reference`.
    For instance, if the `schema_kind` is `grpc+proto` the `schema_reference` is the protobuf definition of the service.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Service(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class MetadataEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Value: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Value] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        URL_FIELD_NUMBER: builtins.int
        SCHEMA_KIND_FIELD_NUMBER: builtins.int
        SCHEMA_REFERENCE_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        url: typing.Text
        schema_kind: typing.Text
        schema_reference: typing.Text
        @property
        def metadata(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Value]: ...
        def __init__(self,
            *,
            url: typing.Text = ...,
            schema_kind: typing.Text = ...,
            schema_reference: typing.Text = ...,
            metadata: typing.Optional[typing.Mapping[typing.Text, global___Value]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["metadata",b"metadata","schema_kind",b"schema_kind","schema_reference",b"schema_reference","url",b"url"]) -> None: ...

    SERVICES_FIELD_NUMBER: builtins.int
    @property
    def services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DiscoverFulfillment.Service]:
        """The list of services provided by the application"""
        pass
    def __init__(self,
        *,
        services: typing.Optional[typing.Iterable[global___DiscoverFulfillment.Service]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["services",b"services"]) -> None: ...
global___DiscoverFulfillment = DiscoverFulfillment

class InspectIntent(google.protobuf.message.Message):
    """*
    Inspect Intent

    The inspection query is a simple wildcard query language expecting dot notations as namespace separators.
    For more details see the ADR `docs/adr/ctp2-/0015-inspection.md`
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    QUERY_FIELD_NUMBER: builtins.int
    query: typing.Text
    def __init__(self,
        *,
        query: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["query",b"query"]) -> None: ...
global___InspectIntent = InspectIntent

class InspectFulfillment(google.protobuf.message.Message):
    """*
    Inspect Fulfillment

    Returns a list of entries containing methods, properties and events that match the query.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Entry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class ItemsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text
            @property
            def value(self) -> global___Value: ...
            def __init__(self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___Value] = ...,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

        PATH_FIELD_NUMBER: builtins.int
        ITEMS_FIELD_NUMBER: builtins.int
        path: typing.Text
        @property
        def items(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Value]: ...
        def __init__(self,
            *,
            path: typing.Text = ...,
            items: typing.Optional[typing.Mapping[typing.Text, global___Value]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["items",b"items","path",b"path"]) -> None: ...

    ENTRIES_FIELD_NUMBER: builtins.int
    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InspectFulfillment.Entry]: ...
    def __init__(self,
        *,
        entries: typing.Optional[typing.Iterable[global___InspectFulfillment.Entry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entries",b"entries"]) -> None: ...
global___InspectFulfillment = InspectFulfillment

class InvokeIntent(google.protobuf.message.Message):
    """*
    Invoke Intent

    The invoke intent is used to invoke a method on the application through the chariott runtime.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COMMAND_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    command: typing.Text
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Value]: ...
    def __init__(self,
        *,
        command: typing.Text = ...,
        args: typing.Optional[typing.Iterable[global___Value]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["args",b"args","command",b"command"]) -> None: ...
global___InvokeIntent = InvokeIntent

class InvokeFulfillment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RETURN_FIELD_NUMBER: builtins.int
    def __init__(self,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["return",b"return"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["return",b"return"]) -> None: ...
global___InvokeFulfillment = InvokeFulfillment

class Value(google.protobuf.message.Message):
    """*
    Value

    The value is a wrapper around multiple value types. In case you don't
    find the type you need, you can use the `any` field to pass a custom
    value type.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NULL_FIELD_NUMBER: builtins.int
    ANY_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    INT32_FIELD_NUMBER: builtins.int
    INT64_FIELD_NUMBER: builtins.int
    FLOAT32_FIELD_NUMBER: builtins.int
    FLOAT64_FIELD_NUMBER: builtins.int
    STRING_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    LIST_FIELD_NUMBER: builtins.int
    MAP_FIELD_NUMBER: builtins.int
    BLOB_FIELD_NUMBER: builtins.int
    null: global___NullValue.ValueType
    @property
    def any(self) -> google.protobuf.any_pb2.Any: ...
    bool: builtins.bool
    int32: builtins.int
    int64: builtins.int
    float32: builtins.float
    float64: builtins.float
    string: typing.Text
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def list(self) -> global___List: ...
    @property
    def map(self) -> global___Map: ...
    @property
    def blob(self) -> global___Blob: ...
    def __init__(self,
        *,
        null: global___NullValue.ValueType = ...,
        any: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        bool: builtins.bool = ...,
        int32: builtins.int = ...,
        int64: builtins.int = ...,
        float32: builtins.float = ...,
        float64: builtins.float = ...,
        string: typing.Text = ...,
        timestamp: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        list: typing.Optional[global___List] = ...,
        map: typing.Optional[global___Map] = ...,
        blob: typing.Optional[global___Blob] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["any",b"any","blob",b"blob","bool",b"bool","float32",b"float32","float64",b"float64","int32",b"int32","int64",b"int64","list",b"list","map",b"map","null",b"null","string",b"string","timestamp",b"timestamp","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["any",b"any","blob",b"blob","bool",b"bool","float32",b"float32","float64",b"float64","int32",b"int32","int64",b"int64","list",b"list","map",b"map","null",b"null","string",b"string","timestamp",b"timestamp","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["null","any","bool","int32","int64","float32","float64","string","timestamp","list","map","blob"]]: ...
global___Value = Value

class Blob(google.protobuf.message.Message):
    """*
    Blob

    The blob message is primarily used to pass around binary data that can be
    described by a mime type.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MEDIA_TYPE_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    media_type: typing.Text
    bytes: builtins.bytes
    def __init__(self,
        *,
        media_type: typing.Text = ...,
        bytes: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bytes",b"bytes","media_type",b"media_type"]) -> None: ...
global___Blob = Blob

class List(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Value]: ...
    def __init__(self,
        *,
        value: typing.Optional[typing.Iterable[global___Value]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["value",b"value"]) -> None: ...
global___List = List

class Map(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> global___Value: ...
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___Value] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    MAP_FIELD_NUMBER: builtins.int
    @property
    def map(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Value]: ...
    def __init__(self,
        *,
        map: typing.Optional[typing.Mapping[typing.Text, global___Value]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["map",b"map"]) -> None: ...
global___Map = Map
