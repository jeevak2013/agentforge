docs/design/01_Runtime_Sequence_Diagrams.md
AgentForge Runtime Sequence Diagrams
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

1. Purpose
This document defines the runtime execution flows for AgentForge.
While the Runtime Architecture document defines runtime components and responsibilities, this document defines:
Runtime behavior
Component interactions
State transitions
Data flow
Failure handling
Completion handling
This document serves as the primary implementation blueprint for Sprint 1.

2. Runtime Overview
The AgentForge runtime follows an Agentic Execution Loop.
Core Pattern:
Think
↓
Tool Call
↓
Observe
↓
Update State
↓
Update Memory
↓
Continue
The runtime remains in this loop until:
Task completed
Task failed
Task cancelled
Runtime limits exceeded

3. Runtime Components
Participating Components
User
API Layer
TaskManager
AgentRuntime
StateManager
PlannerManager
ProviderManager
ToolExecutor
SecurityManager
MemoryManager
CompletionManager
MetricsCollector
AuditLogger
Database

4. Task Lifecycle States
Task State Machine
CREATED
↓
PLANNING
↓
RUNNING
↓
WAITING_FOR_TOOL
↓
RUNNING
↓
COMPLETED

Possible Alternative Paths
RUNNING
↓
FAILED
RUNNING
↓
CANCELLED
RUNNING
↓
WAITING_FOR_HUMAN

5. Sequence Diagram 1 — Task Creation
Objective:
Create a new task.
Flow:
User
↓
POST /tasks
↓
API Layer
↓
TaskManager
↓
PostgreSQL
↓
Task Created

Database Writes
tasks
Initial Status:
CREATED

Output
task_id
workspace_id

6. Sequence Diagram 2 — Runtime Initialization
Objective:
Prepare runtime execution.
Flow:
TaskManager
↓
AgentRuntime
↓
Create ExecutionContext
↓
Create AgentState
↓
Initialize Metrics
↓
Initialize Audit Trail

ExecutionContext
Contains:
task_id
workspace_id
provider
model
start_time

AgentState
Contains:
messages
tool_history
plan
status
iteration_count

7. Sequence Diagram 3 — Planning Phase
Objective:
Generate initial execution plan.
Flow:
AgentRuntime
↓
PlannerManager
↓
ProviderManager
↓
LLM
↓
Plan Generated
↓
Plan Stored

State Transition
CREATED
↓
PLANNING
↓
RUNNING

Database Writes
plans
plan_steps

Example Plan
Create project structure
Create application
Create tests
Execute tests
Complete task

8. Sequence Diagram 4 — First Reasoning Cycle
Objective:
Obtain first runtime decision.
Flow:
AgentRuntime
↓
Build Context
↓
ProviderManager
↓
LLM
↓
Response

Context Includes
Objective
Messages
Plan
Memory
Tool History
Workspace Metadata

Possible Outputs
Tool Call
Plan Update
Completion Request
Text Response

9. Sequence Diagram 5 — Tool Execution
Objective:
Execute a requested tool.
Flow:
Tool Request
↓
SecurityManager
↓
Validation
↓
ToolExecutor
↓
Tool Result

Security Validation
Tool Exists
Schema Valid
Arguments Valid
Workspace Allowed
Policy Allowed

Database Writes
tool_calls
audit_logs

10. Sequence Diagram 6 — File Read Example
Flow:
LLM
↓
read_file(main.py)
↓
SecurityManager
↓
Path Validation
↓
ReadFileTool
↓
File Contents
↓
Tool Result

Audit Log
READ_FILE
SUCCESS

11. Sequence Diagram 7 — File Write Example
Flow:
LLM
↓
write_file(main.py)
↓
SecurityManager
↓
Path Validation
↓
WriteFileTool
↓
File Saved
↓
Tool Result

Audit Log
WRITE_FILE
SUCCESS

12. Sequence Diagram 8 — Command Execution Example
Flow:
LLM
↓
execute_command(pytest)
↓
SecurityManager
↓
Command Policy Engine
↓
Command Executor
↓
Command Output

Possible Outcomes
SUCCESS
FAILED
BLOCKED

Audit Log
EXECUTE_COMMAND

13. Sequence Diagram 9 — Observe Phase
Objective:
Process tool results.
Flow:
Tool Result
↓
StateManager
↓
MemoryManager
↓
MetricsCollector
↓
AuditLogger

State Updates
Tool History
Messages
Iteration Count

Memory Updates
Observation Memory
Summary Memory

Metrics Updates
Tool Count
Execution Time

14. Sequence Diagram 10 — Runtime Loop
Core Runtime Flow
while not completed:
think()

execute_tool()

observe()

update_memory()

continue()


State Transition
RUNNING
↓
WAITING_FOR_TOOL
↓
RUNNING
Repeated until completion.

15. Sequence Diagram 11 — Completion Request
Objective:
Handle attempt_completion.
Flow:
LLM
↓
attempt_completion
↓
CompletionManager
↓
Validation

Validation Checks
Plan Completed
No Pending Tool Calls
No Critical Failures
Runtime Limits Not Violated

Possible Outcomes
COMPLETED
REJECTED

16. Sequence Diagram 12 — Task Completion
Flow:
CompletionManager
↓
Update Task Status
↓
Store Metrics
↓
Store Audit Records
↓
Notify API
↓
Task Complete

State Transition
RUNNING
↓
COMPLETED

Database Updates
tasks
metrics
audit_logs

17. Sequence Diagram 13 — Provider Failure
Flow:
Provider Call
↓
Failure
↓
Retry Policy
↓
ProviderManager

Possible Outcomes
Retry
Fallback Provider
Task Failure

State Transition
RUNNING
↓
FAILED

18. Sequence Diagram 14 — Tool Failure
Flow:
Tool Execution
↓
Exception
↓
Tool Result (Failure)
↓
Observation Phase

Agent Receives
Failure Details
Stack Trace Summary
Error Message

Agent May
Retry
Choose Alternative Tool
Abort Task

19. Sequence Diagram 15 — Security Violation
Flow:
Tool Request
↓
SecurityManager
↓
Policy Violation
↓
Execution Blocked

Examples
Outside Workspace
Blocked Command
Unauthorized MCP Tool

State Transition
RUNNING
↓
SECURITY_BLOCKED
or
RUNNING
↓
WAITING_FOR_HUMAN

20. Sequence Diagram 16 — Human Approval
Flow:
Agent Action
↓
Approval Required
↓
ApprovalManager
↓
User

Possible Outcomes
Approved
Rejected
Expired

State Transition
RUNNING
↓
WAITING_FOR_HUMAN
↓
RUNNING

21. Sequence Diagram 17 — Runtime Cancellation
Flow:
User
↓
Cancel Task
↓
TaskManager
↓
AgentRuntime
↓
Graceful Shutdown

State Transition
RUNNING
↓
CANCELLED

22. Sequence Diagram 18 — Metrics Collection
Metrics Captured
Task Duration
Tool Calls
Provider Calls
Token Usage
Cost
Success Rate
Failure Rate

Storage
metrics table
AgentOps Platform

23. Sequence Diagram 19 — Audit Trail
Events Logged
Task Created
Plan Generated
Tool Executed
Command Executed
Approval Requested
Task Completed
Task Failed

Storage
audit_logs

24. Future Multi-Agent Sequence
Phase 8
Planner Agent
↓
Task Breakdown
↓
Coder Agent
↓
Reviewer Agent
↓
Tester Agent
↓
Completion
Shared Components
Memory
Metrics
Plans

25. Runtime Sequence Summary
User
↓
API
↓
TaskManager
↓
Runtime Initialization
↓
Planning
↓
Reasoning
↓
Tool Execution
↓
Observation
↓
Memory Update
↓
Completion Validation
↓
Metrics
↓
Audit
↓
Task Complete

26. Design Principles
The runtime execution model must remain:
Deterministic
Observable
Auditable
Secure
Provider Agnostic
Domain Agnostic
Extensible
Every runtime action must pass through the sequence flows defined in this document.
Future implementations must conform to these execution patterns.

