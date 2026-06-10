from src.agentforge.providers.models.provider_capabilities import ProviderCapabilities


def test_provider_capabilities_defaults():
    """Test default values of ProviderCapabilities."""
    caps = ProviderCapabilities()
    assert caps.supports_streaming is False
    assert caps.supports_vision is False
    assert caps.supports_tools is False
    assert caps.supports_function_calling is False
    assert caps.supports_json_mode is False


def test_provider_capabilities_assignment():
    """Test explicit assignment of capabilities."""
    caps = ProviderCapabilities(
        supports_streaming=True,
        supports_vision=True,
        supports_tools=True,
        supports_function_calling=False,
        supports_json_mode=True,
    )
    assert caps.supports_streaming is True
    assert caps.supports_vision is True
    assert caps.supports_tools is True
    assert caps.supports_function_calling is False
    assert caps.supports_json_mode is True
