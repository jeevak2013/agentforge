# docs/implementation/04_ExecutionContext.md

# Execution Context Specification

Version: 1.0

Status: Approved

Sprint: Sprint-01 Runtime Foundation

---

# Purpose

ExecutionContext is the runtime container used during task execution.

It encapsulates all information required by the Runtime to process a task.

The ExecutionContext is passed throughout the runtime lifecycle.

---

# Architecture Position

Task
↓
ExecutionContext
↓
Runtime
↓
Provider
↓
Completion

---

# Responsibilities

Store current task.

Store runtime metadata.

Store provider configuration.

Store execution variables.

Store runtime state information.

Provide a single runtime object passed between components.

---

# Design Principles

Single Source of Runtime Truth

Immutable Task Identity

Observable

Extensible

Provider Agnostic

Future Tool Compatible

Future MCP Compatible

---

# Entity Definition

ExecutionContext

Fields

task

provider_name

model_name

runtime_metadata

started_at

current_iteration

max_iterations

execution_id

---

# Field Specifications

task

Type

Task

Required

Yes

Purpose

Current task being executed.

---

execution_id

Type

UUID

Required

Yes

Purpose

Unique execution instance identifier.

Example

A task may be retried multiple times.

Each execution receives a unique execution_id.

---

provider_name

Type

str

Purpose

Active provider.

Examples

OpenAI

Anthropic

Ollama

MockProvider

---

model_name

Type

str

Purpose

Selected model.

Examples

gpt-5

claude-opus

llama3

mock-model

---

started_at

Type

datetime

Purpose

Execution start timestamp.

---

current_iteration

Type

int

Purpose

Current runtime loop iteration.

Default

0

---

max_iterations

Type

int

Purpose

Safety limit.

Default

100

Future

Configurable

---

runtime_metadata

Type

dict[str, Any]

Purpose

Execution-specific metadata.

Examples

Token Counts

Runtime Flags

Debug Information

Environment Data

---

# Runtime Usage

Runtime receives:

ExecutionContext

↓

Uses Context

↓

Updates Context

↓

Returns Context

---

# Iteration Tracking

Purpose

Prevent infinite loops.

Example

Iteration 1

↓

Iteration 2

↓

Iteration 3

↓

...

↓

Iteration 100

↓

Abort

---

# Safety Rules

current_iteration

cannot exceed

max_iterations

---

Runtime must terminate if limit reached.

---

# Provider Integration

ExecutionContext supplies:

provider_name

model_name

to ProviderManager.

---

# Observability Requirements

Track

Execution ID

Provider

Model

Iteration Count

Execution Duration

---

Metrics

Runtime Duration

Average Iterations

Max Iterations Reached

Provider Usage

---

# Future Extensions

Reserved Fields

memory_context

conversation_context

tool_results

approval_state

mcp_context

retrieval_results

agent_assignments

knowledge_graph_results

---

# Example

ExecutionContext

execution_id:
550e8400-e29b-41d4-a716-446655440111

task:
Build Calculator API

provider_name:
MockProvider

model_name:
mock-model

started_at:
2026-06-03T10:00:00Z

current_iteration:
0

max_iterations:
100

runtime_metadata:
{}

---

# Pydantic Model

ExecutionContext(BaseModel)

Fields

execution_id: UUID

task: Task

provider_name: str

model_name: str

started_at: datetime

current_iteration: int

max_iterations: int

runtime_metadata: dict[str, Any]

---

# Acceptance Criteria

ExecutionContext model implemented.

Validation rules implemented.

Serialization supported.

Iteration tracking supported.

Runtime integration supported.

Unit tests passing.

---

# Definition of Done

ExecutionContext approved.

Ready for Runtime integration.

Ready for Provider integration.

Ready for future Tool integration.

Ready for future MCP integration.
