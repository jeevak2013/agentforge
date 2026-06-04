from src.core.state.runtime_state import RuntimeState


def testruntime_state_values():
    assert RuntimeState.CREATED.value == "created"
    assert RuntimeState.PLANNING.value == "planning"
    assert RuntimeState.RUNNING.value == "running"
    assert RuntimeState.COMPLETED.value == "completed"
    assert RuntimeState.FAILED.value == "failed"
    assert RuntimeState.CANCELLED.value == "cancelled"
