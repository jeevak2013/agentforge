import pytest
from src.agentforge.providers.models.provider_usage import ProviderUsage


def test_provider_usage_creation():
    """Test standard creation of ProviderUsage."""
    usage = ProviderUsage(
        prompt_tokens=100,
        completion_tokens=50,
    )
    assert usage.prompt_tokens == 100
    assert usage.completion_tokens == 50


def test_provider_usage_defaults():
    """Test default values of ProviderUsage."""
    usage = ProviderUsage()
    assert usage.prompt_tokens == 0
    assert usage.completion_tokens == 0
    assert usage.total_tokens == 0


def test_provider_usage_total_tokens():
    """Test automatic total_tokens calculation."""
    usage = ProviderUsage(
        prompt_tokens=100,
        completion_tokens=50,
    )
    # Total calculation should trigger automatically
    assert usage.total_tokens == 150


def test_provider_usage_explicit_total_tokens():
    usage = ProviderUsage(
        prompt_tokens=100,
        completion_tokens=50,
        total_tokens=999,
    )

    assert usage.total_tokens == 999
