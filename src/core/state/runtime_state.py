from __future__ import annotations

from enum import Enum


class RuntimeState(str, Enum):
    """
    Represent the lifecycle state of an AgentForge task.
    """

    CREATED = "created"
    PLANNING = "planning"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
