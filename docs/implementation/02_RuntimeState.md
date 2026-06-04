docs/implementation/02_Task_Model.md
Task Model Specification
Version: 1.0
Status: Approved
Sprint: Sprint-01 Runtime Foundation

1. Purpose
The Task entity represents a single unit of agent execution.
Every operation in AgentForge executes within a Task.
Examples:
Build API
Analyze Dataset
Generate Test Cases
Review Pull Request
Create RCM Report

2. Responsibilities
Track execution state
Store metadata
Store results
Store failures
Support auditing
Support observability
Support future multi-agent workflows

3. Entity Overview
Task
↓
Execution Context
↓
Runtime
↓
Provider
↓
Completion

4. Task Lifecycle
CREATED
↓
PLANNING
↓
RUNNING
↓
COMPLETED
or
FAILED
or
CANCELLED

5. Task Model
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

6. Field Definitions
task_id
Type
UUID
Purpose
Globally unique identifier
Example
550e8400-e29b-41d4-a716-446655440000

title
Type
String
Purpose
Human-readable task name
Example
Build FastAPI CRUD Service

description
Type
String
Purpose
Detailed task objective
Example
Create FastAPI CRUD API with PostgreSQL integration.

status
Type
RuntimeState
Purpose
Current execution state

created_at
Type
Datetime
Purpose
Creation timestamp

updated_at
Type
Datetime
Purpose
Last modification timestamp

completed_at
Type
Datetime | None
Purpose
Completion timestamp

result
Type
String | None
Purpose
Final task output

error
Type
String | None
Purpose
Failure details

metadata
Type
Dictionary
Purpose
Extensible runtime information

7. RuntimeState Enumeration
CREATED
PLANNING
RUNNING
COMPLETED
FAILED
CANCELLED

Reserved Future States
WAITING_FOR_PROVIDER
WAITING_FOR_TOOL
WAITING_FOR_APPROVAL
WAITING_FOR_HUMAN

8. Validation Rules
title
Required
Maximum 255 characters

description
Optional
Maximum 10000 characters

status
Must be valid RuntimeState

task_id
Must be UUID

9. Example Instance
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
result:
None
error:
None

10. Persistence Mapping
Database Table
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

11. Audit Requirements
Track
Creation
State Changes
Completion
Failures
Cancellation

All transitions must be logged.

12. Observability Requirements
Metrics
Task Count
Success Rate
Failure Rate
Average Duration
Cancellation Rate

Integrated With
AgentOps
Observability Platform

13. Future Extensions
Priority
Owner
Tags
Parent Task
Child Tasks
Agent Assignment
Approval Status
Execution Cost
Token Usage

14. Python Model
Pydantic BaseModel
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
metadata: dict

15. Acceptance Criteria
Task can be created.
Task validates successfully.
Task serializes to JSON.
Task supports persistence.
Task supports state transitions.
Task supports observability hooks.

16. Definition of Done
Task model implemented.
Unit tests passing.
Validation implemented.
Serialization implemented.
Documentation updated.
Task entity approved for Runtime integration.

