from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import AsyncGenerator

from src.agentforge.infrastructure.providers.provider_models import (
    ProviderRequest,
    ProviderResponse,
)


@dataclass
class ProviderHealth:
    status: str
    latency_ms: int
    provider: str


class BaseProvider(ABC):
    @abstractmethod
    async def generate(self, request: ProviderRequest) -> ProviderResponse:
        """Generates a response from the provider based on the given request."""
        pass

    @abstractmethod
    async def stream(self, request: ProviderRequest) -> AsyncGenerator[str, None]:
        """Streams a response from the provider based on the given request."""
        pass

    @abstractmethod
    async def health_check(self) -> ProviderHealth:
        """Performs a health check on the provider and returns its status."""
        pass

    @abstractmethod
    def count_tokens(self, request: ProviderRequest) -> int:
        """Counts the number of tokens in the given request."""
        pass

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Returns the name of the provider."""
        pass
