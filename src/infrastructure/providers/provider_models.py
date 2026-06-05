from __future__ import annotations

from pydantic import BaseModel, Field
from datetime import UTC, datetime
from enum import Enum
from uuid import UUID, uuid4
from typing import Any


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL_CALL = "tool_call"
    TOOL_RESULT = "tool_result"


class Message(BaseModel):
    role: MessageRole
    content: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    metadata: dict[str, Any] = Field(default_factory=dict)


class FinishReason(str, Enum):
    COMPLETED = "completed"
    STOP = "stop"
    MAX_TOKENS = "max_tokens"
    TOOL_CALL = "tool_call"
    CONTENT_FILTERED = "content_filtered"
    ERROR = "error"
    UNKNOWN = "unknown"


class ProviderUsage(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    estimated_cost: float = 0.0


class ProviderRequest(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    execution_id: UUID
    messages: list[Message]
    system_prompt: str = ""
    model: str
    temperature: float = 0.2
    max_tokens: int = 4000
    metadata: dict[str, Any] = Field(default_factory=dict)


class ProviderResponse(BaseModel):
    response_id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    content: str
    finish_reason: FinishReason
    usage: ProviderUsage = Field(default_factory=ProviderUsage)
    provider: str
    model: str
    metadata: dict[str, Any] = Field(default_factory=dict)
