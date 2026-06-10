from pydantic import BaseModel, Field


class ProviderConfiguration(BaseModel):
    provider_name: str
    api_key: str | None = None
    base_url: str | None = None
    timeout_seconds: int = Field(default=60, gt=0)
    max_retries: int = Field(default=3, ge=0)
    enabled: bool = True
