from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from src.agentforge.core.state.runtime_state import RuntimeState


class Task(BaseModel):
    task_id: UUID = Field(default_factory=uuid4)

    title: str

    description: str | None = None

    status: RuntimeState = RuntimeState.CREATED

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    completed_at: datetime | None = None

    result: str | None = None

    error: str | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)
