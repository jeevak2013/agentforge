from __future__ import annotations

from typing import AsyncGenerator
from uuid import uuid4

import pytest

from src.agentforge.infrastructure.providers.base_provider import (
    BaseProvider,
    ProviderHealth,
)
from src.agentforge.infrastructure.providers.provider_models import (
    ProviderRequest,
    ProviderResponse,
)


def test_base_provider_cannot_instantiate():

    with pytest.raises(
        TypeError, match="Can't instantiate abstract class BaseProvider"
    ):
        BaseProvider()


def test_incomplete_mock_provider_fails():
    class IncompleteProvider(BaseProvider):
        @property
        def provider_name(self) -> str:
            return "IncompleteProvider"

    with pytest.raises(
        TypeError,
        match="Can't instantiate abstract class IncompleteProvider",
    ):
        IncompleteProvider()


def test_mock_provider_will_implement_contract():
    class ValidMockProvider(BaseProvider):
        @property
        def provider_name(self) -> str:
            return "ValidMockProvider"

        async def generate(self, request: ProviderRequest) -> ProviderResponse:
            pass

        async def stream(self, request: ProviderRequest) -> AsyncGenerator[str, None]:
            yield "streaming response"

        async def health_check(self) -> ProviderHealth:
            return ProviderHealth(
                status="healthy", latency_ms=15, provider=self.provider_name
            )

        def count_tokens(self, request: ProviderRequest) -> int:
            return 100

    provider = ValidMockProvider()

    assert isinstance(provider, BaseProvider)
    assert provider.provider_name == "ValidMockProvider"
    assert (
        provider.count_tokens(
            ProviderRequest(
                task_id=uuid4(), execution_id=uuid4(), messages=[], model="test-model"
            )
        )
        == 100
    )
