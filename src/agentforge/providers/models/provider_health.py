from enum import StrEnum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProviderHealthStatus(StrEnum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"


class ProviderHealth(BaseModel):
    status: ProviderHealthStatus = ProviderHealthStatus.UNKNOWN

    response_time_ms: float = Field(default=0.0, ge=0.0)
    last_check: Optional[datetime] = None
    error_message: Optional[str] = None
