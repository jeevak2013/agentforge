from __future__ import annotations

from datetime import UTC, datetime

from src.core.state.runtime_state import RuntimeState
from src.core.task.task import Task
from src.infrastructure.providers.provider_models import ProviderResponse


class CompletionManager:
    @staticmethod
    def validate(response: ProviderResponse) -> bool:
        return bool(response and response.content)

    @staticmethod
    def complete(task: Task, response: ProviderResponse) -> Task:
        task.status = RuntimeState.COMPLETED
        task.result = response.content

        task.completed_at = datetime.now(UTC)
        task.updated_at = datetime.now(UTC)

        return task

    @staticmethod
    def fail(task: Task, error: Exception | str) -> Task:
        task.status = RuntimeState.FAILED
        task.error = str(error)

        task.completed_at = datetime.now(UTC)
        task.updated_at = datetime.now(UTC)

        return task

    @staticmethod
    def is_complete(task: Task) -> bool:
        return task.status in {
            RuntimeState.COMPLETED,
            RuntimeState.FAILED,
            RuntimeState.CANCELLED,
        }
