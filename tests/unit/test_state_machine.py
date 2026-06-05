from __future__ import annotations

import pytest

from core.state.runtime_state import RuntimeState
from core.state.state_machine import TaskStateMachine


def test_valid_transition():

    machine = TaskStateMachine(initial_state=RuntimeState.CREATED)

    machine.transition(RuntimeState.PLANNING)
    assert machine.current_state() == RuntimeState.PLANNING


def test_invalid_transition():

    machine = TaskStateMachine(initial_state=RuntimeState.CREATED)

    with pytest.raises(ValueError):
        machine.transition(RuntimeState.RUNNING)


def test_terminal_state_completed():

    machine = TaskStateMachine(initial_state=RuntimeState.COMPLETED)

    assert machine.is_terminal() is True

    with pytest.raises(ValueError):
        machine.transition(RuntimeState.RUNNING)


def test_terminal_state_failed():

    machine = TaskStateMachine(initial_state=RuntimeState.FAILED)

    assert machine.is_terminal() is True
    with pytest.raises(ValueError):
        machine.transition(RuntimeState.PLANNING)


def test_terminal_state_cancelled():

    machine = TaskStateMachine(initial_state=RuntimeState.CANCELLED)

    assert machine.is_terminal() is True
    with pytest.raises(ValueError):
        machine.transition(RuntimeState.CREATED)


def test_can_transition():

    machine = TaskStateMachine(initial_state=RuntimeState.PLANNING)

    assert machine.can_transition(RuntimeState.RUNNING) is True
    assert machine.can_transition(RuntimeState.COMPLETED) is False
    assert machine.can_transition(RuntimeState.CREATED) is False
