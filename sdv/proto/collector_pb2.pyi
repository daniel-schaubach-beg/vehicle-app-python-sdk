"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation

This program and the accompanying materials are made available under the
terms of the Apache License, Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.

SPDX-License-Identifier: Apache-2.0
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sdv.proto.types_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class UpdateDatapointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DatapointsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> sdv.databroker.v1.types_pb2.Datapoint: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: sdv.databroker.v1.types_pb2.Datapoint | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DATAPOINTS_FIELD_NUMBER: builtins.int
    @property
    def datapoints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, sdv.databroker.v1.types_pb2.Datapoint]: ...
    def __init__(
        self,
        *,
        datapoints: collections.abc.Mapping[builtins.int, sdv.databroker.v1.types_pb2.Datapoint] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["datapoints", b"datapoints"]) -> None: ...

global___UpdateDatapointsRequest = UpdateDatapointsRequest

class UpdateDatapointsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ErrorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: sdv.databroker.v1.types_pb2.DatapointError.ValueType
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: sdv.databroker.v1.types_pb2.DatapointError.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ERRORS_FIELD_NUMBER: builtins.int
    @property
    def errors(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, sdv.databroker.v1.types_pb2.DatapointError.ValueType]:
        """If empty, everything went well"""
    def __init__(
        self,
        *,
        errors: collections.abc.Mapping[builtins.int, sdv.databroker.v1.types_pb2.DatapointError.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["errors", b"errors"]) -> None: ...

global___UpdateDatapointsReply = UpdateDatapointsReply

class StreamDatapointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DatapointsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> sdv.databroker.v1.types_pb2.Datapoint: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: sdv.databroker.v1.types_pb2.Datapoint | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DATAPOINTS_FIELD_NUMBER: builtins.int
    @property
    def datapoints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, sdv.databroker.v1.types_pb2.Datapoint]: ...
    def __init__(
        self,
        *,
        datapoints: collections.abc.Mapping[builtins.int, sdv.databroker.v1.types_pb2.Datapoint] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["datapoints", b"datapoints"]) -> None: ...

global___StreamDatapointsRequest = StreamDatapointsRequest

class StreamDatapointsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ErrorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        value: sdv.databroker.v1.types_pb2.DatapointError.ValueType
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: sdv.databroker.v1.types_pb2.DatapointError.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ERRORS_FIELD_NUMBER: builtins.int
    @property
    def errors(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, sdv.databroker.v1.types_pb2.DatapointError.ValueType]:
        """If empty, everything went well"""
    def __init__(
        self,
        *,
        errors: collections.abc.Mapping[builtins.int, sdv.databroker.v1.types_pb2.DatapointError.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["errors", b"errors"]) -> None: ...

global___StreamDatapointsReply = StreamDatapointsReply

class RegisterDatapointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIST_FIELD_NUMBER: builtins.int
    @property
    def list(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RegistrationMetadata]: ...
    def __init__(
        self,
        *,
        list: collections.abc.Iterable[global___RegistrationMetadata] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["list", b"list"]) -> None: ...

global___RegisterDatapointsRequest = RegisterDatapointsRequest

class RegistrationMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    DATA_TYPE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CHANGE_TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the data point
    (e.g. "Vehicle.Cabin.Seat.Row1.Pos1.Position" or "Vehicle.Speed")
    """
    data_type: sdv.databroker.v1.types_pb2.DataType.ValueType
    description: builtins.str
    change_type: sdv.databroker.v1.types_pb2.ChangeType.ValueType
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        data_type: sdv.databroker.v1.types_pb2.DataType.ValueType = ...,
        description: builtins.str = ...,
        change_type: sdv.databroker.v1.types_pb2.ChangeType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["change_type", b"change_type", "data_type", b"data_type", "description", b"description", "name", b"name"]) -> None: ...

global___RegistrationMetadata = RegistrationMetadata

class RegisterDatapointsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class ResultsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """Maps each data point name passed in RegisterDatapointsRequest to a data point id"""
    def __init__(
        self,
        *,
        results: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["results", b"results"]) -> None: ...

global___RegisterDatapointsReply = RegisterDatapointsReply
