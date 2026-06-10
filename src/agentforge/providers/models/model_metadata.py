from pydantic import BaseModel, Field

from src.agentforge.providers.models.provider_capabilities import ProviderCapabilities


class ModelMetadata(BaseModel):
    model_id: str
    display_name: str
    provider_name: str
    context_window: int = Field(ge=0)
    max_output_tokens: int = Field(ge=0)
    capabilities: ProviderCapabilities
