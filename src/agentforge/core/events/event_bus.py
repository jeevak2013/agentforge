from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Callable

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Event:
    """
    Represents an immutable transactional event inside the agent platform loop.
    """

    event_type: str
    payload: dict[str, Any] = field(default_factory=dict)


class EventBus:
    """
    Central synchronous event backbone for system-wide AgentOps, metrics, and audit trails.
    """

    def __init__(self) -> None:
        """
        Initializes the event registry with an empty routing handler structure.
        """
        self._handlers: dict[str, list[Callable[[Event], Any]]] = {}

    def subscribe(self, event_type: str, handler: Callable[[Event], Any]) -> None:
        """
        Registers a callback handler to listen to a specified event type.

        Args:
            event_type: The string signature of the target event topic.
            handler: The callback executable that accepts the Event payload.
        """
        if event_type not in self._handlers:
            self._handlers[event_type] = []

        if handler not in self._handlers[event_type]:
            self._handlers[event_type].append(handler)

    def unsubscribe(self, event_type: str, handler: Callable[[Event], Any]) -> None:
        """
        Removes a registered callback handler from an execution topic list.

        Args:
            event_type: The topic signature the listener wants to disconnect from.
            handler: The functional reference originally attached during subscription.
        """
        if event_type in self._handlers:
            try:
                self._handlers[event_type].remove(handler)
            except ValueError:
                logger.debug(
                    "Handler was not registered under this event type"
                )  # Handler was not registered under this event type

            # Clean up empty list keys to optimize data structure tracking
            if not self._handlers[event_type]:
                del self._handlers[event_type]

    def publish(self, event: Event) -> None:
        """
        Dispatches an event payload sequentially to all subscribed listeners.

        If any handler raises an exception, it is caught immediately and logged via
        the central logging framework. This prevents telemetry or reporting failures
        from disrupting the active core runtime loop.

        Args:
            event: The immutable event payload entity containing the type and telemetry metadata.
        """
        if not event or event.event_type not in self._handlers:
            return

        # Iterate over a shallow copy of the handlers list to prevent runtime modifications
        for handler in list(self._handlers[event.event_type]):
            try:
                handler(event)
            except Exception as e:
                logger.error(
                    f"Error in event handler for target '{event.event_type}': {e}",
                    exc_info=True,
                )
