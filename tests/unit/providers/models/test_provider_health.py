from src.agentforge.providers.models.provider_health import (
    ProviderHealth,
    ProviderHealthStatus,
)

import pytest
from pydantic import ValidationError
from datetime import datetime


def test_provider_health_creation():
    health = ProviderHealth(status=ProviderHealthStatus.HEALTHY, response_time_ms=150)
    assert health.status == ProviderHealthStatus.HEALTHY
    assert health.response_time_ms == 150


def test_provider_health_defaults():
    health = ProviderHealth()

    assert health.status == ProviderHealthStatus.UNKNOWN
    assert health.response_time_ms == 0
    assert health.last_check is None
    assert health.error_message is None


def test_provider_health_error_message():
    health = ProviderHealth(
        status=ProviderHealthStatus.UNHEALTHY, error_message="Test error message"
    )

    assert health.status == ProviderHealthStatus.UNHEALTHY
    assert health.error_message == "Test error message"


def test_provider_health_negative_response_time():
    with pytest.raises(ValidationError):
        ProviderHealth(status=ProviderHealthStatus.HEALTHY, response_time_ms=-1)


def test_provider_health_last_check():
    now = datetime.now()

    health = ProviderHealth(
        status=ProviderHealthStatus.HEALTHY,
        last_check=now,
    )

    assert health.last_check == now
