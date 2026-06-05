from __future__ import annotations

from uuid import UUID, uuid4

from src.infrastructure.providers.provider_models import (
    FinishReason,
    Message,
    MessageRole,
    ProviderRequest,
    ProviderResponse,
    ProviderUsage,
)


def test_message_creation():

    msg = Message(role=MessageRole.USER, content="Hello, Agent!")

    assert msg.role == MessageRole.USER
    assert msg.content == "Hello, Agent!"
    assert msg.timestamp is not None
    assert msg.metadata == {}


def test_provider_usage_defaults():

    usage = ProviderUsage()

    assert usage.input_tokens == 0
    assert usage.output_tokens == 0
    assert usage.total_tokens == 0
    assert usage.estimated_cost == 0.0


def test_provider_request_creation():

    task_id = uuid4()
    exec_id = uuid4()
    msg = Message(role=MessageRole.USER, content="Write a python script.")

    request = ProviderRequest(
        task_id=task_id, execution_id=exec_id, messages=[msg], model="gpt-4o"
    )

    assert request.task_id == task_id
    assert request.execution_id == exec_id
    assert len(request.messages) == 1
    assert request.model == "gpt-4o"
    assert request.temperature == 0.2  # Default value
    assert request.max_tokens == 4000  # Default value


def test_request_id_generated():

    request = ProviderRequest(
        task_id=uuid4(), execution_id=uuid4(), messages=[], model="gpt-4o"
    )

    assert isinstance(request.request_id, UUID)


def test_provider_response_creation():

    req_id = uuid4()

    response = ProviderResponse(
        request_id=req_id,
        content="Here is your code...",
        finish_reason=FinishReason.COMPLETED,
        provider="openai",
        model="gpt-4o",
    )

    assert response.request_id == req_id
    assert response.content == "Here is your code..."
    assert response.finish_reason == FinishReason.COMPLETED
    assert response.provider == "openai"
    assert response.model == "gpt-4o"
    assert isinstance(response.usage, ProviderUsage)


def test_response_id_generated():

    response = ProviderResponse(
        request_id=uuid4(),
        content="Testing ID",
        finish_reason=FinishReason.STOP,
        provider="anthropic",
        model="claude-3-opus",
    )

    assert isinstance(response.response_id, UUID)


def test_finish_reason_values():

    assert FinishReason.COMPLETED.value == "completed"
    assert FinishReason.STOP.value == "stop"
    assert FinishReason.MAX_TOKENS.value == "max_tokens"
    assert FinishReason.TOOL_CALL.value == "tool_call"
    assert FinishReason.ERROR.value == "error"
