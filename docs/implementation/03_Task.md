# docs/implementation/03_Task.md

# Task Entity Specification

Version: 1.0

Status: Approved

Sprint: Sprint-01 Runtime Foundation

---

# Purpose

Task represents a single unit of agent execution.

Every request submitted to AgentForge creates exactly one Task.

The Task is the primary runtime entity and acts as the root aggregate for execution state, metadata, results, and observability.

---

# Responsibilities

Store task identity.

Store execution state.

Store task metadata.

Store execution result.

Store failure information.

Support observability.

Support persistence.

Support future multi-agent execution.

---

# Architecture Position

User Request
↓
Task
↓
Runtime
↓
Provider
↓
Completion

---

# Entity Definition

Task

Fields

task_id

title

description

status

created_at

updated_at

completed_at

result

error

metadata

---

# Field Specifications

task_id

Type

UUID

Purpose

Globally unique identifier.

Example

550e8400-e29b-41d4-a716-446655440000

---

title

Type

String

Required

Yes

Purpose

Human-readable task name.

Example

Build FastAPI CRUD Service

---

description

Type

String | None

Required

No

Purpose

Detailed task objective.

Example

Create CRUD API with PostgreSQL and authentication.

---

status

Type

RuntimeState

Required

Yes

Purpose

Current task lifecycle state.

Default

CREATED

---

created_at

Type

datetime

Required

Yes

Purpose

Task creation timestamp.

---

updated_at

Type

datetime

Required

Yes

Purpose

Last update timestamp.

---

completed_at

Type

datetime | None

Purpose

Task completion timestamp.

---

result

Type

str | None

Purpose

Final task output.

Examples

Generated Code

Generated Report

Completion Summary

---

error

Type

str | None

Purpose

Failure details.

Examples

Provider Timeout

Validation Error

Runtime Failure

---

metadata

Type

dict[str, Any]

Purpose

Extensible task attributes.

Examples

Provider

Model

User Id

Tags

Environment

---

# State Ownership

Task owns RuntimeState.

Example

task.status

↓

CREATED

↓

PLANNING

↓

RUNNING

↓

COMPLETED

---

# Task Lifecycle

Task Created
↓
Planning
↓
Running
↓
Completed

or

Failed

or

Cancelled

---

# Business Rules

task_id immutable.

created_at immutable.

status must be valid RuntimeState.

completed_at set only when task finishes.

result and error mutually exclusive.

---

# Validation Rules

title required.

title max length = 255.

description max length = 10000.

metadata must be JSON serializable.

---

# Pydantic Model

Task(BaseModel)

Fields

task_id: UUID

title: str

description: str | None

status: RuntimeState

created_at: datetime

updated_at: datetime

completed_at: datetime | None

result: str | None

error: str | None

metadata: dict[str, Any]

---

# Persistence Mapping

Table

tasks

Columns

task_id

title

description

status

created_at

updated_at

completed_at

result

error

metadata

---

# Observability Requirements

Metrics

Task Count

Task Success Count

Task Failure Count

Task Duration

Task State Changes

---

# Audit Requirements

Record

Task Creation

State Changes

Completion

Failure

Cancellation

---

# Example

Task

task_id:
123e4567-e89b-12d3-a456-426614174000

title:
Build Calculator API

description:
Create REST API supporting add, subtract, multiply and divide.

status:
CREATED

created_at:
2026-06-03T10:00:00Z

updated_at:
2026-06-03T10:00:00Z

completed_at:
null

result:
null

error:
null

metadata:
{}

---

# Future Extensions

priority

owner

cost

token_usage

approval_status

parent_task_id

child_tasks

assigned_agent

evaluation_score

---

# Acceptance Criteria

Task model implemented.

Validation rules implemented.

Serialization supported.

Persistence supported.

Observability hooks defined.

Unit tests passing.

---

# Definition of Done

Task entity approved.

Ready for Runtime integration.

Ready for State Machine integration.

Ready for Persistence integration.
