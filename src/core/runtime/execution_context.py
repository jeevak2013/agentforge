from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field

from src.core.task.task import Task


class ExecutionContext(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    execution_id: UUID = Field(default_factory=uuid4)

    task: Task

    provider_name: str

    model_name: str

    started_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    current_iteration: int = 0

    max_iterations: int = 100

    runtime_metadata: dict[str, Any] = Field(default_factory=dict)
