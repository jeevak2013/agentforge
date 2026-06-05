from __future__ import annotations

from uuid import UUID

import pytest

from src.core.runtime.execution_context import ExecutionContext
from src.core.task.task import Task


@pytest.fixture
def sample_task_fixture():
    return Task(title="Integrate LLM API", description="Set up Anthropic Client")


def test_execution_context_creation(sample_task_fixture):
    ctx = ExecutionContext(
        task=sample_task_fixture,
        provider_name="anthropic",
        model_name="claude-3-5-sonnet",
    )

    assert ctx.provider_name == "anthropic"
    assert ctx.model_name == "claude-3-5-sonnet"
    assert ctx.task.title == "Integrate LLM API"


def test_execution_id_generated(sample_task_fixture):
    ctx_1 = ExecutionContext(
        task=sample_task_fixture, provider_name="openai", model_name="gpt-4o"
    )
    ctx_2 = ExecutionContext(
        task=sample_task_fixture, provider_name="openai", model_name="gpt-4o"
    )

    assert isinstance(ctx_1.execution_id, UUID)
    assert ctx_1.execution_id != ctx_2.execution_id  # இரண்டு ஐடியும் வெவ்வேறாக இருக்க வேண்டும்


def test_default_iteration_zero(sample_task_fixture):
    ctx = ExecutionContext(
        task=sample_task_fixture, provider_name="gemini", model_name="gemini-1.5-pro"
    )

    assert ctx.current_iteration == 0


def test_default_max_iterations(sample_task_fixture):
    ctx = ExecutionContext(
        task=sample_task_fixture, provider_name="gemini", model_name="gemini-1.5-pro"
    )

    assert ctx.max_iterations == 100


def test_runtime_metadata_default_dict(sample_task_fixture):
    ctx = ExecutionContext(
        task=sample_task_fixture, provider_name="ollama", model_name="llama3"
    )

    assert isinstance(ctx.runtime_metadata, dict)
    assert len(ctx.runtime_metadata) == 0
