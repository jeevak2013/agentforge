from __future__ import annotations

import pytest
from datetime import datetime, timezone
from uuid import uuid4

from src.core.completion.completion_manager import CompletionManager
from src.core.state.runtime_state import RuntimeState
from src.core.task.task import Task
from src.infrastructure.providers.provider_models import ProviderResponse, FinishReason


def test_validate_success():

    response = ProviderResponse(
        request_id=uuid4(),
        content="Successfully processed execution block.",
        finish_reason=FinishReason.COMPLETED,
        provider="test_provider",
        model="test_model",
    )

    validation_result = CompletionManager.validate(response)

    assert validation_result


def test_complete_task():

    task = Task(title="Test completion Task")
    task.status = RuntimeState.RUNNING

    response = ProviderResponse(
        request_id=uuid4(),
        content="Final generated application codebase artifact.",
        finish_reason=FinishReason.COMPLETED,
        provider="test_provider",
        model="test_model",
    )

    # Act
    updated_task = CompletionManager.complete(task, response)

    # Assert
    assert updated_task.status == RuntimeState.COMPLETED
    assert updated_task.result == "Final generated application codebase artifact."
    assert updated_task.completed_at is not None
    assert updated_task.updated_at is not None
    assert isinstance(updated_task.completed_at, datetime)
    assert updated_task.completed_at.tzinfo == timezone.utc


def test_fail_task():

    task = Task(title="Test Failure Task")
    task.status = RuntimeState.RUNNING

    execution_error = RuntimeError(
        "Workspace path security boundary sandbox isolation violation."
    )

    # Act
    updated_task = CompletionManager.fail(task, error=execution_error)

    # Assert
    assert updated_task.status == RuntimeState.FAILED
    assert updated_task.error == (
        "Workspace path security boundary sandbox isolation violation."
    )
    assert updated_task.completed_at is not None
    assert updated_task.updated_at is not None
    assert isinstance(updated_task.completed_at, datetime)
    assert updated_task.completed_at.tzinfo == timezone.utc


@pytest.mark.parametrize(
    "terminal_state",
    [
        RuntimeState.COMPLETED,
        RuntimeState.FAILED,
        RuntimeState.CANCELLED,
    ],
)
def test_is_complete_true(terminal_state):

    task = Task(title="Test Terminal State")  # Provide a title
    task.status = terminal_state

    # Act & Assert
    assert CompletionManager.is_complete(task) is True


@pytest.mark.parametrize(
    "active_state",
    [
        RuntimeState.CREATED,
        RuntimeState.PLANNING,
        RuntimeState.RUNNING,
    ],
)
def test_is_complete_false(active_state):

    # Arrange
    task = Task(title="Test Active State")  # Provide a title
    task.status = active_state

    # Act & Assert
    assert CompletionManager.is_complete(task) is False
