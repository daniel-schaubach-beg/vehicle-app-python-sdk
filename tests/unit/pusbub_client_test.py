# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

""" Tests for methods in PubSubClient """
import os

os.environ["SDV_MIDDLEWARE_TYPE"] = "native"

import sys
from unittest import mock

import pytest

from sdv import config
from sdv.config import Config
from sdv.base import Middleware
from sdv.dapr.pubsub import DaprClient
from sdv.native.mqtt import MqttClient
from sdv.native.middleware import NativeMiddleware

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))


@pytest.fixture(autouse=True)
def reset():
    config._config = Config("native")
    config.middleware = NativeMiddleware()


@pytest.mark.asyncio
async def test_for_subscribe_topic():
    # config.DISABLE_DAPR = True

    # client = get_pubsub_client_instance()
    # with mock.patch.object(
    #     client.pubsub_client,
    #     "register_topic",
    #     new_callable=mock.AsyncMock,
    # ) as mocked_client:
    #     await client.subscribe_topic("/test/native", None)
    #     assert isinstance(client.pubsub_client, MqttClient)
    #     mocked_client.assert_called_once_with("/test/native", None)

    # config.DISABLE_DAPR = False
    middleware = get_middleware_instance()
    with mock.patch.object(
        middleware.pubsub_client,
        "register_topic",
        new_callable=mock.AsyncMock,
    ) as mocked_client:
        await middleware.pubsub_client.register_topic("/test/dapr", None)
        assert isinstance(middleware.pubsub_client, MqttClient)
        mocked_client.assert_called_once_with("/test/dapr", None)


@pytest.mark.asyncio
async def test_for_get_publish_event():
    # config.DISABLE_DAPR = True

    middleware = get_middleware_instance()
    with mock.patch.object(
        middleware.pubsub_client,
        "publish_event",
        new_callable=mock.AsyncMock,
    ) as mocked_client:
        await middleware.pubsub_client.publish_event("/test/native", "message")
        mocked_client.assert_called_once_with("/test/native", "message")


def get_middleware_instance() -> Middleware:
    return config.middleware