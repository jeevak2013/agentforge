import pytest
from pydantic import ValidationError

from src.agentforge.providers.models.provider_configuration import ProviderConfiguration


def test_provider_configuration_creation():
    config = ProviderConfiguration(
        provider_name="openai",
        api_key="sk-123",
        base_url="https://api.openai.com",
        timeout_seconds=30,
        max_retries=5,
        enabled=True,
    )
    assert config.provider_name == "openai"
    assert config.api_key == "sk-123"
    assert config.base_url == "https://api.openai.com"
    assert config.timeout_seconds == 30
    assert config.max_retries == 5
    assert config.enabled


def test_provider_configuration_defaults():
    config = ProviderConfiguration(provider_name="ollama")

    assert config.api_key is None
    assert config.base_url is None
    assert config.timeout_seconds == 60
    assert config.max_retries == 3
    assert config.enabled is True


def test_provider_configuration_validation():
    with pytest.raises(ValidationError):
        ProviderConfiguration(provider_name="test", timeout_seconds=0)


def test_provider_configuration_negative_max_retries():
    with pytest.raises(ValidationError):
        ProviderConfiguration(provider_name="test-provider", max_retries=-1)


def test_provider_configuration_zero_retries():
    config = ProviderConfiguration(
        provider_name="openai",
        max_retries=0,
    )

    assert config.max_retries == 0
