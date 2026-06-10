from pydantic import BaseModel


class ProviderCapabilities(BaseModel):
    supports_streaming: bool = False
    supports_vision: bool = False
    supports_tools: bool = False
    supports_function_calling: bool = False
    supports_json_mode: bool = False
