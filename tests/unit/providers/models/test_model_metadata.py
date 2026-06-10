import pytest
from pydantic import ValidationError

from src.agentforge.providers.models.model_metadata import ModelMetadata
from src.agentforge.providers.models.provider_capabilities import ProviderCapabilities


def test_model_metadata_creation():
    caps = ProviderCapabilities()
    model_metadata = ModelMetadata(
        model_id="gpt-4o",
        display_name="GPT-4o",
        provider_name="openai",
        context_window=128000,
        max_output_tokens=4096,
        capabilities=caps,
    )

    assert model_metadata.model_id == "gpt-4o"
    assert model_metadata.display_name == "GPT-4o"
    assert model_metadata.provider_name == "openai"
    assert model_metadata.context_window == 128000
    assert model_metadata.max_output_tokens == 4096


def test_model_metadata_capabilities():
    caps = ProviderCapabilities(
        supports_streaming=True,
        supports_vision=True,
    )

    model_metadata = ModelMetadata(
        model_id="gemini-2.5-pro",
        display_name="Gemini 2.5 Pro",
        provider_name="google",
        context_window=1000000,
        max_output_tokens=8192,
        capabilities=caps,
    )

    assert model_metadata.capabilities.supports_streaming is True
    assert model_metadata.capabilities.supports_vision is True
    assert model_metadata.capabilities.supports_tools is False


def test_model_metadata_validation():
    caps = ProviderCapabilities()

    with pytest.raises(ValidationError):
        ModelMetadata(
            model_id="test-model",
            display_name="Test Model",
            provider_name="test provider",
            context_window=-1,
            max_output_tokens=4096,
            capabilities=caps,
        )
