from pydantic import BaseModel

from src.agentforge.providers.models.provider_usage import (
    ProviderUsage,
)


class ProviderResponse(BaseModel):
    content: str
    model_name: str
    usage: ProviderUsage
    finish_reason: str = "stop"
