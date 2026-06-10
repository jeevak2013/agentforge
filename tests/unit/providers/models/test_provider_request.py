import pytest
from pydantic import ValidationError
from src.agentforge.providers.models.provider_request import ProviderRequest


def test_provider_request_creation():

    request = ProviderRequest(
        prompt="Explain quantum physics",
        system_prompt="You are a professor.",
        model_name="gpt-4o",
        temperature=0.2,
        max_tokens=2048,
    )
    assert request.prompt == "Explain quantum physics"
    assert request.system_prompt == "You are a professor."
    assert request.model_name == "gpt-4o"
    assert request.temperature == 0.2
    assert request.max_tokens == 2048


def test_provider_request_defaults():
    """Verify default values are applied correctly."""
    request = ProviderRequest(prompt="Test", model_name="gpt-4o")
    assert request.temperature == 0.2
    assert request.max_tokens == 4096
    assert request.system_prompt is None


def test_provider_request_invalid_temperature():
    """Verify invalid temperature raises ValidationError."""
    with pytest.raises(ValidationError):
        ProviderRequest(
            prompt="Test",
            model_name="gpt-4o",
            temperature=-1,
        )


def test_provider_request_temperature_too_high():
    """Verify temperature = 3 raises ValidationError."""
    with pytest.raises(ValidationError):
        ProviderRequest(prompt="Test", model_name="gpt-4o", temperature=3.0)


def test_provider_request_invalid_max_tokens():
    """Verify invalid max_tokens raises ValidationError."""
    with pytest.raises(ValidationError):
        ProviderRequest(
            prompt="Test",
            model_name="gpt-4o",
            max_tokens=0,  # Must be gt=0
        )
