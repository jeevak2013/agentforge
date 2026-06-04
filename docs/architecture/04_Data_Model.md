docs/architecture/04_Data_Model.md
AgentForge Data Model Architecture
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

1. Purpose
This document defines the logical and physical data architecture for AgentForge.
It specifies:
Core entities
Relationships
Persistence strategy
Storage responsibilities
Future scalability considerations
The data model serves as the foundation for:
Runtime State
APIs
Memory Systems
AgentOps
Evaluation
Security

2. Data Architecture Principles
Principle 1
Single Source of Truth
Each entity must have one authoritative location.

Principle 2
Separation of Concerns
Structured data and vector data must remain separate.

Principle 3
Event Traceability
All important actions must be traceable.

Principle 4
Runtime State ≠ Persistent State
Redis is temporary.
PostgreSQL is authoritative.

3. Storage Architecture
AgentForge uses four storage systems.

PostgreSQL
Purpose:
Structured transactional data.
Stores:
Users
Tasks
Plans
Messages
Tool Calls
Tool Results
Metrics
Audit Logs

Redis
Purpose:
Runtime state.
Stores:
Active agent states
Queues
Locks
Streaming sessions

Qdrant
Purpose:
Semantic retrieval.
Stores:
Embeddings
Code indexes
Long-term memory vectors

MinIO
Purpose:
Object storage.
Stores:
Uploaded files
Artifacts
Generated reports
Snapshots

4. Core Domain Model
High-Level Relationships
User
↓
Task
↓
AgentRun
↓
Messages
↓
ToolCalls
↓
ToolResults
Task
↓
Plan
↓
PlanSteps
Task
↓
Memory
Task
↓
Metrics
Task
↓
AuditLogs

5. User Entity
Purpose:
Represents a platform user.

Fields
user_id
email
name
role
status
created_at
updated_at

Relationships
User
↓
Many Tasks

6. Task Entity
Purpose:
Represents a unit of work.
Example:
"Create FastAPI Calculator API"

Fields
task_id
user_id
workspace_id
objective
status
provider
model
created_at
completed_at

Task Status
CREATED
PLANNING
RUNNING
WAITING_FOR_TOOL
WAITING_FOR_HUMAN
FAILED
COMPLETED

Relationships
Task
↓
Messages
Task
↓
Plans
Task
↓
AgentRuns
Task
↓
Memory
Task
↓
Metrics

7. AgentRun Entity
Purpose:
Represents a runtime execution instance.
A task may be executed multiple times.

Fields
run_id
task_id
status
started_at
ended_at
total_iterations
tokens_used
cost

Relationships
AgentRun
↓
ToolCalls
AgentRun
↓
Metrics

8. Message Entity
Purpose:
Conversation history.

Fields
message_id
task_id
role
content
metadata
created_at

Roles
system
user
assistant
tool

Relationships
Task
↓
Many Messages

9. ToolCall Entity
Purpose:
Tracks every tool invocation.

Fields
tool_call_id
run_id
tool_name
arguments
status
started_at
ended_at

Status
PENDING
RUNNING
SUCCESS
FAILED
BLOCKED

Relationships
ToolCall
↓
ToolResult

10. ToolResult Entity
Purpose:
Store tool execution output.

Fields
tool_result_id
tool_call_id
success
output
metadata
created_at

Examples
File contents
Command output
Validation results
Search results

11. Plan Entity
Purpose:
Store task plans.

Fields
plan_id
task_id
version
status
created_at

Relationships
Plan
↓
PlanSteps

12. PlanStep Entity
Purpose:
Track execution progress.

Fields
step_id
plan_id
description
order_no
status
created_at
completed_at

Status
TODO
IN_PROGRESS
DONE
BLOCKED

13. Memory Entity
Purpose:
Persistent memory storage.

Fields
memory_id
task_id
memory_type
content
created_at

Memory Types
SHORT_TERM
SUMMARY
RETRIEVAL
OBSERVATION
DECISION

Relationships
Task
↓
Many Memory Records

14. Embedding Entity
Stored in Qdrant
Purpose:
Semantic retrieval.

Metadata
embedding_id
task_id
source_type
source_id
vector
created_at

Source Types
MESSAGE
MEMORY
CODE
DOCUMENT

15. Metrics Entity
Purpose:
Support AgentOps.

Fields
metric_id
task_id
run_id
tokens_input
tokens_output
tool_calls
execution_time
cost
created_at

16. Evaluation Entity
Purpose:
Measure quality.

Fields
evaluation_id
task_id
score
feedback
evaluator
created_at

Examples
Task Success
Code Quality
Review Quality

17. AuditLog Entity
Purpose:
Security traceability.

Fields
audit_id
task_id
action
resource
result
user_id
timestamp

Examples
READ_FILE
WRITE_FILE
EXECUTE_COMMAND
APPROVE_ACTION

18. ApprovalRequest Entity
Purpose:
Human approval workflow.

Fields
approval_id
task_id
action
status
requested_at
approved_at
approved_by

Status
PENDING
APPROVED
REJECTED
EXPIRED

19. Workspace Entity
Purpose:
Represent isolated workspaces.

Fields
workspace_id
task_id
path
status
created_at

Relationships
Workspace
↓
One Task

20. Future Multi-Agent Entities
Phase 8

Agent
Fields
agent_id
role
model
status

Roles
Planner
Coder
Reviewer
Tester

AgentMessage
Purpose:
Agent-to-agent communication.

Fields
message_id
sender_agent
receiver_agent
content
timestamp

21. Future MCP Entities
Phase 9

MCPServer
Fields
server_id
name
status
trust_level

MCPTool
Fields
tool_id
server_id
tool_name
permissions
risk_level

22. Physical Storage Mapping
PostgreSQL
Users
Tasks
Plans
Messages
Tool Calls
Tool Results
Metrics
Evaluations
Audit Logs
Approvals
Workspaces

Redis
AgentState
ExecutionContext
Queues
Locks
Streams

Qdrant
Embeddings
Code Indexes
Retrieval Memory

MinIO
Artifacts
Files
Reports
Snapshots

23. Design Principles
The AgentForge data model must remain:
Normalized
Auditable
Scalable
Provider-Agnostic
Domain-Agnostic
Future-Proof
All future implementations must conform to the entities and relationships defined in this document.

