from __future__ import annotations

import pytest
from unittest.mock import MagicMock

from src.agentforge.core.runtime.agent_runtime import AgentRuntime
from src.agentforge.core.completion.completion_manager import CompletionManager
from src.agentforge.core.events.event_bus import Event, EventBus
from src.agentforge.core.task.task import Task
from src.agentforge.core.state.runtime_state import RuntimeState
from src.agentforge.infrastructure.providers.mock_provider import MockProvider


@pytest.mark.asyncio
async def test_runtime_execute_success():
    """
    Verify successful execution path: Task moves from CREATED to COMPLETED.
    """
    # Arrange
    mock_provider = MockProvider()
    completion_manager = CompletionManager()
    event_bus = EventBus()
    runtime = AgentRuntime(mock_provider, completion_manager, event_bus)

    task = Task(
        title="Runtime Success Test",
        status=RuntimeState.CREATED,
    )

    # Track events
    events_received = []
    event_bus.subscribe("task_started", lambda e: events_received.append(e.event_type))
    event_bus.subscribe(
        "task_completed", lambda e: events_received.append(e.event_type)
    )

    # Act
    updated_task = await runtime.execute(task)

    # Assert
    assert updated_task.status == RuntimeState.COMPLETED
    assert updated_task.result is not None
    assert "task_started" in events_received
    assert "task_completed" in events_received


@pytest.mark.asyncio
async def test_runtime_execute_failure():
    """
    Verify failure path: Runtime catches provider exception and sets task to FAILED.
    """
    # Arrange
    # Assuming MockProvider can be configured to fail via a mock
    mock_provider = MagicMock(spec=MockProvider)
    mock_provider.provider_name = "MockProvider"
    # Configure mock to raise an exception
    mock_provider.generate.side_effect = Exception("Provider API Connection Timeout")

    completion_manager = CompletionManager()
    event_bus = EventBus()
    runtime = AgentRuntime(mock_provider, completion_manager, event_bus)

    task = Task(
        title="Runtime Failure Test",
        status=RuntimeState.RUNNING,
    )

    # Track events
    events_received = []
    event_bus.subscribe("task_failed", lambda e: events_received.append(e.event_type))

    # Act
    updated_task = await runtime.execute(task)

    # Assert
    assert updated_task.status == RuntimeState.FAILED
    assert updated_task.error is not None
    assert "Provider API Connection Timeout" in updated_task.error
    assert "task_failed" in events_received


@pytest.mark.asyncio
async def test_event_publishing_lifecycle():
    """
    Deep verification of event bus subscription during runtime execution.
    """
    bus = EventBus()
    # Mocking handler to verify exact call parameters
    handler = MagicMock()
    bus.subscribe("task_started", handler)

    provider = MockProvider()
    runtime = AgentRuntime(provider, CompletionManager(), bus)
    task = Task(title="Event Lifecycle Test")

    await runtime.execute(task)

    # Assert
    handler.assert_called_once()
    args = handler.call_args[0][0]
    assert isinstance(args, Event)
    assert args.event_type == "task_started"
    assert args.payload["task_id"] == str(task.task_id)
