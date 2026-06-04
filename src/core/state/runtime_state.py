from enum import Enum


class RuntimeState(str, Enum):
    """
    REpresent the lifecycle state of an Agentforge task.
    """

    CREATED = "created"
    PLANNING = "planning"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
