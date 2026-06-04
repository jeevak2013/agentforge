# docs/implementation/06_Provider_Models.md

# Provider Models Specification

Version: 1.0

Status: Approved

Sprint: Sprint-01 Runtime Foundation

Related ADR

ADR-002 Provider Abstraction

---

# Purpose

Provider Models define the contract between:

AgentRuntime

and

Provider Layer

The Runtime must only communicate using these models.

No provider-specific objects may enter the Runtime.

---

# Architecture

AgentRuntime
↓
ProviderRequest
↓
Provider
↓
ProviderResponse
↓
AgentRuntime

---

# Design Principles

Provider Agnostic

Strongly Typed

Observable

Extensible

Streaming Compatible

Future Tool Compatible

Future Multi-Agent Compatible

---

# Core Models

ProviderRequest

ProviderResponse

ProviderUsage

FinishReason

ProviderHealth

---

# ProviderRequest

Purpose

Represents a request sent from Runtime to a provider.

---

Fields

request_id

task_id

execution_id

messages

system_prompt

model

temperature

max_tokens

metadata

---

# ProviderRequest Definition

request_id

Type

UUID

Purpose

Unique request identifier

---

task_id

Type

UUID

Purpose

Associated task

---

execution_id

Type

UUID

Purpose

Associated execution

---

messages

Type

list[Message]

Purpose

Conversation payload

---

system_prompt

Type

str

Purpose

System instructions

---

model

Type

str

Purpose

Requested model

Examples

gpt-5

claude-opus

llama3

---

temperature

Type

float

Purpose

Sampling control

Range

0.0 → 2.0

---

max_tokens

Type

int

Purpose

Maximum response tokens

---

metadata

Type

dict

Purpose

Provider-specific extensions

---

# ProviderResponse

Purpose

Represents a provider response.

---

Fields

response_id

request_id

content

finish_reason

usage

model

provider

metadata

---

# ProviderResponse Definition

response_id

Type

UUID

---

request_id

Type

UUID

---

content

Type

str

Purpose

Generated content

---

finish_reason

Type

FinishReason

---

usage

Type

ProviderUsage

---

model

Type

str

---

provider

Type

str

---

metadata

Type

dict

---

# FinishReason

Purpose

Standardize provider completion behavior.

---

Values

COMPLETED

STOP

MAX_TOKENS

ERROR

TOOL_CALL

CONTENT_FILTERED

UNKNOWN

---

# ProviderUsage

Purpose

Track token consumption.

Supports

Observability

Cost Analysis

AgentOps

---

Fields

input_tokens

output_tokens

total_tokens

estimated_cost

---

# ProviderHealth

Purpose

Runtime health checking.

---

Fields

provider

status

latency_ms

checked_at

error

---

# Health Status

HEALTHY

DEGRADED

UNAVAILABLE

---

# Message Model

Purpose

Provider-independent message representation.

---

Fields

role

content

timestamp

metadata

---

# Roles

SYSTEM

USER

ASSISTANT

TOOL_CALL

TOOL_RESULT

---

# Runtime Flow

ExecutionContext
↓
ProviderRequest
↓
Provider
↓
ProviderResponse
↓
Runtime

---

# Observability Requirements

Track

Provider Calls

Provider Latency

Token Usage

Cost

Failure Rate

Model Usage

---

# Example ProviderRequest

{
"request_id": "123",
"task_id": "456",
"execution_id": "789",
"model": "mock-model",
"temperature": 0.2,
"max_tokens": 2000
}

---

# Example ProviderResponse

{
"response_id": "999",
"request_id": "123",
"content": "Task completed successfully",
"finish_reason": "COMPLETED",
"provider": "MockProvider"
}

---

# Future Extensions

Streaming Chunks

Tool Calls

Structured Outputs

Multimodal Inputs

Image Outputs

Reasoning Traces

Function Calling

---

# Validation Rules

Request ID required

Response ID required

Model required

Messages required

FinishReason required

---

# Acceptance Criteria

ProviderRequest implemented

ProviderResponse implemented

ProviderUsage implemented

FinishReason implemented

ProviderHealth implemented

Unit tests passing

Serialization supported

---

# Definition of Done

Provider models approved.

Ready for BaseProvider implementation.

Ready for MockProvider implementation.

Ready for OpenAI Provider implementation.

Ready for Anthropic Provider implementation.

Ready for Ollama Provider implementation.
