import pytest
from datetime import datetime

from src.agentforge.providers.errors.provider_error import (
    ProviderError,
    ProviderAuthenticationError,
    ProviderRateLimitError,
    ProviderSafetyFilterError,
    ProviderUnknownError,
    ProviderStreamingError,
    ProviderTimeoutError,
    ProviderUnavailableError,
    ProviderAuthorizationError,
    ProviderConfigurationError,
    ProviderContextWindowExceededError,
    ProviderResponseError,
    ProviderValidationError,
)


def test_provider_error_creation():
    err = ProviderError(message="Fail", provider_name="openai", error_code="ERR001")
    assert err.message == "Fail"
    assert err.provider_name == "openai"
    assert err.retryable is False
    assert err.timestamp.tzinfo is not None


def test_timezone_validation():
    """Verify naive datetime raises ValueError."""
    with pytest.raises(ValueError, match="timestamp must be timezone-aware UTC"):
        ProviderError(
            message="x",
            provider_name="y",
            timestamp=datetime.now(),  # Naive datetime
        )


def test_provider_error_serialization():
    err = ProviderError(message="Fail", provider_name="openai")
    data = err.to_dict()
    assert data["message"] == "Fail"
    assert "timestamp" in data


def test_provider_error_deserialization():
    data = {
        "message": "Fail",
        "provider_name": "openai",
        "error_code": "ERR001",
        "retryable": False,
        "timestamp": "2026-06-11T09:00:00+00:00",
    }
    err = ProviderError.from_dict(data)
    assert err.message == "Fail"
    assert err.retryable is False


def test_round_trip_serialization():
    """Verify to_dict and from_dict round-trip."""
    original_err = ProviderRateLimitError(
        message="Rate limit hit", provider_name="openai", error_code="429"
    )

    serialized = original_err.to_dict()
    assert serialized["error_type"] == "ProviderRateLimitError"

    restored = ProviderError.from_dict(serialized)
    assert restored.message == original_err.message
    assert restored.retryable is True
    assert isinstance(restored, ProviderRateLimitError)


def test_retry_classification():
    assert ProviderRateLimitError(message="x", provider_name="y").retryable is True
    assert ProviderTimeoutError(message="x", provider_name="y").retryable is True
    assert ProviderUnavailableError(message="x", provider_name="y").retryable is True
    assert ProviderStreamingError(message="x", provider_name="y").retryable is True


def test_non_retryable_classification():
    assert (
        ProviderAuthenticationError(message="x", provider_name="y").retryable is False
    )
    assert ProviderUnknownError(message="x", provider_name="y").retryable is False


def test_inheritance_validation():
    subclasses = [
        ProviderAuthenticationError,
        ProviderAuthorizationError,
        ProviderRateLimitError,
        ProviderTimeoutError,
        ProviderUnavailableError,
        ProviderValidationError,
        ProviderConfigurationError,
        ProviderContextWindowExceededError,
        ProviderResponseError,
        ProviderStreamingError,
        ProviderSafetyFilterError,
        ProviderUnknownError,
    ]
    for sub in subclasses:
        assert issubclass(sub, ProviderError)
