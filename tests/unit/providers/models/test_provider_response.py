from src.agentforge.providers.models.provider_response import (
    ProviderResponse,
)

from src.agentforge.providers.models.provider_usage import (
    ProviderUsage,
)


def test_provider_response_creation():
    """Verify all supplied values persist."""
    usage = ProviderUsage(prompt_tokens=10, completion_tokens=5)
    response = ProviderResponse(
        content="Hello world",
        model_name="gpt-4o",  # Changed model_name to model
        usage=usage,
        finish_reason="stop",  # Changed string to FinishReason enum member
    )

    assert response.content == "Hello world"
    assert response.model_name == "gpt-4o"
    assert response.usage == usage
    assert response.finish_reason == "stop"


def test_provider_response_defaults():
    """Verify default values (finish_reason='stop')."""
    usage = ProviderUsage(prompt_tokens=10, completion_tokens=5)
    response = ProviderResponse(
        content="Testing",
        model_name="gpt-4o",
        usage=usage,
        finish_reason="stop",
    )
    assert response.finish_reason == "stop"


def test_provider_response_usage():
    """Verify nested ProviderUsage is preserved."""
    nested_usage = ProviderUsage(
        prompt_tokens=100,
        completion_tokens=50,
    )
    response = ProviderResponse(
        content="More tokens",
        model_name="claude-3-sonnet",
        usage=nested_usage,
        finish_reason="stop",
    )

    assert response.usage.prompt_tokens == 100
    assert response.usage.completion_tokens == 50
    assert response.usage.total_tokens == 150
