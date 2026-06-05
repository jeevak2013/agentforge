from __future__ import annotations

from core.state.runtime_state import RuntimeState


class TaskStateMachine:
    ALLOWED_TRANSITIONS: dict[RuntimeState, set[RuntimeState]] = {
        RuntimeState.CREATED: {RuntimeState.PLANNING},
        RuntimeState.PLANNING: {RuntimeState.RUNNING},
        RuntimeState.RUNNING: {
            RuntimeState.COMPLETED,
            RuntimeState.FAILED,
            RuntimeState.CANCELLED,
        },
        RuntimeState.COMPLETED: set(),
        RuntimeState.FAILED: set(),
        RuntimeState.CANCELLED: set(),
    }

    def __init__(self, initial_state: RuntimeState = RuntimeState.CREATED):
        self._state = initial_state

    def current_state(self) -> RuntimeState:
        return self._state

    def can_transition(self, new_state: RuntimeState) -> bool:
        allowed_next_states = self.ALLOWED_TRANSITIONS.get(self._state, set())
        return new_state in allowed_next_states

    def transition(self, new_state: RuntimeState) -> None:
        if not self.can_transition(new_state):
            raise ValueError(
                f"Invalid state transition from {self._state} to {new_state}"
            )
        self._state = new_state

    def is_terminal(self) -> bool:
        return len(self.ALLOWED_TRANSITIONS.get(self._state, set())) == 0
