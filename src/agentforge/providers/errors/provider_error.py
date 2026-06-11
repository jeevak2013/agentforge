from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any, Dict, Type


@dataclass
class ProviderError(Exception):
    message: str
    provider_name: str
    error_code: str = "PROVIDER_ERROR"
    retryable: bool = False
    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self):
        """Ensure timestamp is timezone-aware and UTC."""
        if self.timestamp.tzinfo is None:
            raise ValueError("timestamp must be timezone-aware UTC")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "provider_name": self.provider_name,
            "error_code": self.error_code,
            "retryable": self.retryable,
            "timestamp": self.timestamp.isoformat(),
            "error_type": self.__class__.__name__,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProviderError":
        data_copy = data.copy()
        error_type_name = data_copy.pop("error_type", None)

        target_cls = _ERROR_REGISTRY.get(error_type_name, cls)

        data_copy["timestamp"] = datetime.fromisoformat(data_copy["timestamp"])
        return target_cls(**data_copy)


_ERROR_REGISTRY: Dict[str, Type[ProviderError]] = {
    "ProviderError": ProviderError,
}


@dataclass
class ProviderAuthenticationError(ProviderError):
    pass


@dataclass
class ProviderAuthorizationError(ProviderError):
    pass


@dataclass
class ProviderRateLimitError(ProviderError):
    retryable: bool = True


@dataclass
class ProviderTimeoutError(ProviderError):
    retryable: bool = True


@dataclass
class ProviderUnavailableError(ProviderError):
    retryable: bool = True


@dataclass
class ProviderValidationError(ProviderError):
    pass


@dataclass
class ProviderConfigurationError(ProviderError):
    pass


@dataclass
class ProviderContextWindowExceededError(ProviderError):
    pass


@dataclass
class ProviderResponseError(ProviderError):
    pass


@dataclass
class ProviderStreamingError(ProviderError):
    retryable: bool = True


@dataclass
class ProviderSafetyFilterError(ProviderError):
    pass


@dataclass
class ProviderUnknownError(ProviderError):
    pass


_ERROR_REGISTRY.update(
    {
        "ProviderAuthenticationError": ProviderAuthenticationError,
        "ProviderAuthorizationError": ProviderAuthorizationError,
        "ProviderRateLimitError": ProviderRateLimitError,
        "ProviderTimeoutError": ProviderTimeoutError,
        "ProviderUnavailableError": ProviderUnavailableError,
        "ProviderValidationError": ProviderValidationError,
        "ProviderConfigurationError": ProviderConfigurationError,
        "ProviderContextWindowExceededError": ProviderContextWindowExceededError,
        "ProviderResponseError": ProviderResponseError,
        "ProviderStreamingError": ProviderStreamingError,
        "ProviderSafetyFilterError": ProviderSafetyFilterError,
        "ProviderUnknownError": ProviderUnknownError,
    }
)
