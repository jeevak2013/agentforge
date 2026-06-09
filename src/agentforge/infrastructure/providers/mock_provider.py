from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import AsyncGenerator

from src.agentforge.infrastructure.providers.base_provider import (
    BaseProvider,
    ProviderHealth,
)
from src.agentforge.infrastructure.providers.provider_models import (
    ProviderRequest,
    ProviderResponse,
    FinishReason,
    ProviderUsage,
)


@dataclass
class MockProviderConfig:
    simulate_failure: bool = False
    latency_ms: int = 0
    fixed_response: str = "Task completed successfully."


class MockProvider(BaseProvider):
    def __init__(self, config: MockProviderConfig = None):
        self.config = config or MockProviderConfig()

    async def generate(self, request: ProviderRequest) -> ProviderResponse:
        if self.config.simulate_failure:
            raise RuntimeError("MockProvider simulated failure.")

        if self.config.latency_ms > 0:
            await asyncio.sleep(self.config.latency_ms / 1000)

        return ProviderResponse(
            request_id=request.request_id,
            content=self.config.fixed_response,
            finish_reason=FinishReason.COMPLETED,
            provider=self.provider_name,
            model=request.model,
            usage=ProviderUsage(
                input_tokens=10,
                output_tokens=10,
                total_tokens=20,
                estimated_cost=0.001,
            ),
        )

    async def stream(self, request: ProviderRequest) -> AsyncGenerator[str, None]:
        yield self.config.fixed_response

    async def health_check(self) -> ProviderHealth:
        return ProviderHealth(
            status="healthy" if not self.config.simulate_failure else "unhealthy",
            latency_ms=self.config.latency_ms,
            provider=self.provider_name,
        )

    def count_tokens(self, request: ProviderRequest) -> int:
        all_text = request.system_prompt + " ".join(
            [m.content for m in request.messages]
        )
        return len(all_text) // 4

    @property
    def provider_name(self) -> str:
        return "MockProvider"
