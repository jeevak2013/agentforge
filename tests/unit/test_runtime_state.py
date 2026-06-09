from __future__ import annotations

from src.agentforge.core.state.runtime_state import RuntimeState


def test_runtime_state_values():
    assert RuntimeState.CREATED.value == "created"
    assert RuntimeState.PLANNING.value == "planning"
    assert RuntimeState.RUNNING.value == "running"
    assert RuntimeState.COMPLETED.value == "completed"
    assert RuntimeState.FAILED.value == "failed"
    assert RuntimeState.CANCELLED.value == "cancelled"


def test_runtime_state_is_string_enum():
    assert isinstance(RuntimeState.CREATED.value, str)


def test_runtime_state_member_count():
    assert len(RuntimeState) == 6
