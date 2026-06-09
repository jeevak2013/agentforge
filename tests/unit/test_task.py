"""Unit tests for the :class:`~src.core.task.task.Task` model.

This test suite verifies the core functionality of the ``Task`` class, including:

- Proper creation of a task with title and optional description.
- Automatic assignment of a unique ``task_id`` (UUID).
- Correct default ``status`` set to ``RuntimeState.CREATED``.
- Generation of ``created_at`` timestamps within the creation window.
- Presence of an empty ``metadata`` dictionary by default.
"""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import UUID

import pytest

from src.agentforge.core.state.runtime_state import RuntimeState
from src.agentforge.core.task.task import Task


def test_task_creation():
    """Test that a Task is created with the given title and description."""
    task = Task(title="Test Task", description="This is a test task.")

    assert task.title == "Test Task"
    assert task.description == "This is a test task."


def test_default_state_created():
    """Test that a newly created Task has status set to CREATED by default."""
    task = Task(title="Test Task")

    assert task.status == RuntimeState.CREATED
    assert task.status.value == "created"


def test_metadata_default_dict():
    """Test that a new Task has an empty metadata dictionary by default."""
    task = Task(title="Test Task")

    assert isinstance(task.metadata, dict)
    assert len(task.metadata) == 0


def test_uuid_generated():
    """Test that each Task gets a unique UUID as task_id."""
    task_1 = Task(title="Test Task")
    task_2 = Task(title="Test Task")

    assert isinstance(task_1.task_id, UUID)
    assert isinstance(task_2.task_id, UUID)
    assert task_1.task_id != task_2.task_id


def test_created_at_generated():
    """Test that the created_at timestamp is set between before and after creation times."""
    before_creation = datetime.now(UTC)
    task = Task(title="Test Task")
    after_creation = datetime.now(UTC)

    assert before_creation <= task.created_at <= after_creation
