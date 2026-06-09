from __future__ import annotations

import logging
import pytest

from src.agentforge.core.events.event_bus import Event, EventBus


def test_subscribe() -> None:
    """
    Verify handlers can successfully subscribe to a specific event type.
    """
    # Arrange
    bus = EventBus()
    event_type = "task_created"

    def sample_handler(event: Event) -> None:
        pass

    # Act
    bus.subscribe(event_type, sample_handler)

    # Assert
    assert event_type in bus._handlers
    assert sample_handler in bus._handlers[event_type]
    assert len(bus._handlers[event_type]) == 1


def test_publish() -> None:
    """
    Verify published events trigger their respective subscribed handlers with accurate payloads.
    """
    # Arrange
    bus = EventBus()
    received_events: list[Event] = []

    def tracker_handler(event: Event) -> None:
        received_events.append(event)

    event_type = "task_completed"
    payload = {"task_id": "task-123", "duration_seconds": 4.2}
    test_event = Event(event_type=event_type, payload=payload)

    bus.subscribe(event_type, tracker_handler)

    # Act
    bus.publish(test_event)

    # Assert
    assert len(received_events) == 1
    assert received_events[0].event_type == event_type
    assert received_events[0].payload["task_id"] == "task-123"
    assert received_events[0].payload["duration_seconds"] == 4.2


def test_unsubscribe() -> None:
    """
    Verify a handler can be unregistered and safely stops receiving published events.
    """
    # Arrange
    bus = EventBus()
    call_count = 0

    def counting_handler(event: Event) -> None:
        nonlocal call_count
        call_count += 1

    event_type = "agent_step"
    test_event = Event(event_type=event_type, payload={})

    bus.subscribe(event_type, counting_handler)
    bus.publish(test_event)  # First call

    # Act
    bus.unsubscribe(event_type, counting_handler)
    bus.publish(test_event)  # Should not fire

    # Assert
    assert call_count == 1
    assert event_type not in bus._handlers  # Verifies empty internal key pruning


def test_multiple_subscribers() -> None:
    """
    Verify multiple distinct handlers subscribed to the same event type all execute independently.
    """
    # Arrange
    bus = EventBus()
    execution_order: list[str] = []

    def first_handler(event: Event) -> None:
        execution_order.append("first")

    def second_handler(event: Event) -> None:
        execution_order.append("second")

    event_type = "metrics_flush"
    bus.subscribe(event_type, first_handler)
    bus.subscribe(event_type, second_handler)

    # Act
    bus.publish(Event(event_type=event_type))

    # Assert
    assert len(execution_order) == 2
    assert "first" in execution_order
    assert "second" in execution_order


def test_publish_without_subscribers() -> None:
    """
    Verify publishing an event that has no registered listeners does not raise errors.
    """
    # Arrange
    bus = EventBus()
    unhandled_event = Event(event_type="ghost_event", payload={"data": "isolated"})

    # Act & Assert
    try:
        bus.publish(unhandled_event)
    except Exception as e:
        pytest.fail(
            f"Publishing an unhandled event raised an unexpected exception: {e}"
        )


def test_broken_handler_logging(caplog: pytest.LogCaptureFixture) -> None:
    """
    Verify a failing subscriber logs its exception safely and does not break the execution pool.
    """
    # Arrange
    bus = EventBus()
    executed_normally = False

    def malicious_handler(event: Event) -> None:
        raise ValueError("Simulated diagnostic telemetry channel crash")

    def resilient_handler(event: Event) -> None:
        nonlocal executed_normally
        executed_normally = True

    event_type = "system_alert"
    bus.subscribe(event_type, malicious_handler)
    bus.subscribe(event_type, resilient_handler)

    # Act & Assert
    with caplog.at_level(logging.ERROR):
        try:
            bus.publish(Event(event_type=event_type))
        except Exception as e:
            pytest.fail(f"EventBus execution context leaked an error: {e}")

    # Check downstream handler still processed normally
    assert executed_normally is True

    # Check that error was intercepted and logged accurately
    assert len(caplog.records) == 1
    assert "Error in event handler for target 'system_alert'" in caplog.text
    assert "Simulated diagnostic telemetry channel crash" in caplog.text
