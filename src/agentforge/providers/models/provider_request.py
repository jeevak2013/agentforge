from pydantic import BaseModel, Field


class ProviderRequest(BaseModel):
    prompt: str
    system_prompt: str | None = None
    model_name: str
    temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    max_tokens: int = Field(default=4096, gt=0)
