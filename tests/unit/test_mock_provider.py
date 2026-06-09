from __future__ import annotations

import pytest

from uuid import uuid4

from src.agentforge.infrastructure.providers.mock_provider import (
    MockProvider,
    MockProviderConfig,
)

from src.agentforge.infrastructure.providers.provider_models import (
    Message,
    MessageRole,
    ProviderRequest,
    FinishReason,
)


@pytest.fixture
def mock_provider():

    return MockProvider()


@pytest.fixture
def sample_request():
    return ProviderRequest(
        task_id=uuid4(),
        execution_id=uuid4(),
        messages=[Message(role=MessageRole.USER, content="What is the weather today?")],
        model="mock-model",
    )


@pytest.mark.asyncio
async def test_generate_success(mock_provider, sample_request):
    response = await mock_provider.generate(sample_request)

    assert response.content == "Task completed successfully."
    assert response.finish_reason == FinishReason.COMPLETED
    assert response.provider == "MockProvider"


@pytest.mark.asyncio
async def test_health_check(mock_provider):
    health = await mock_provider.health_check()
    assert health.status == "healthy"
    assert health.provider == "MockProvider"


def test_count_tokens(mock_provider, sample_request):
    count = mock_provider.count_tokens(sample_request)
    assert count > 0


@pytest.mark.asyncio
async def test_simulated_failure(sample_request):
    config = MockProviderConfig(simulate_failure=True)
    provider = MockProvider(config=config)

    with pytest.raises(RuntimeError, match="MockProvider simulated failure"):
        await provider.generate(sample_request)


@pytest.mark.asyncio
async def test_stream(mock_provider, sample_request):
    chunks = []

    async for chunk in mock_provider.stream(sample_request):
        chunks.append(chunk)

    assert len(chunks) == 1
    # ஸ்ட்ரீமிங் லிஸ்ட்டாக வராது, சிங்கிள் மெசேஜாக வரும்
    assert chunks[0] == "Task completed successfully."
