docs/implementation/05_TaskStateMachine.md
Task State Machine Specification
Version: 1.0
Status: Approved
Sprint: Sprint-01 Runtime Foundation

Purpose
The TaskStateMachine controls all valid state transitions for AgentForge tasks.
It guarantees that tasks move through the runtime lifecycle in a predictable and valid manner.
The state machine is the authoritative source of transition validation.

Responsibilities
Validate state transitions.
Reject invalid transitions.
Track current state.
Enforce terminal states.
Support future workflow expansion.
Provide runtime lifecycle consistency.

Architecture Position
Task
↓
TaskStateMachine
↓
Runtime

State Model
RuntimeState
CREATED
PLANNING
RUNNING
COMPLETED
FAILED
CANCELLED

Future Reserved States
WAITING_FOR_PROVIDER
WAITING_FOR_TOOL
WAITING_FOR_APPROVAL
WAITING_FOR_HUMAN
WAITING_FOR_MCP
WAITING_FOR_AGENT

State Diagram
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

Allowed Transitions
CREATED
→ PLANNING

PLANNING
→ RUNNING

RUNNING
→ COMPLETED

RUNNING
→ FAILED

RUNNING
→ CANCELLED

Invalid Transitions
CREATED
→ COMPLETED

CREATED
→ FAILED

PLANNING
→ COMPLETED

COMPLETED
→ RUNNING

FAILED
→ RUNNING

CANCELLED
→ RUNNING

Terminal States
COMPLETED
FAILED
CANCELLED

Terminal states cannot transition.

State Machine Class
TaskStateMachine
Responsibilities
Transition Validation
Current State Tracking
Transition Execution
State Inspection

Public Methods
current_state()
Returns
RuntimeState

can_transition(target_state)
Returns
bool

transition(target_state)
Returns
RuntimeState
Raises Exception on invalid transition.

is_terminal()
Returns
bool

Transition Validation Rules
Rule 1
Current state must exist.

Rule 2
Target state must exist.

Rule 3
Transition must be explicitly allowed.

Rule 4
Terminal states cannot transition.

Example
Current State
CREATED
Target State
PLANNING
Result
SUCCESS

Current State
COMPLETED
Target State
RUNNING
Result
ERROR

Runtime Integration
AgentRuntime
↓
TaskStateMachine
↓
Transition Validation
↓
Task Status Updated

Observability Requirements
Track
State Changes
Transition Counts
Transition Failures
Terminal State Reached

Metrics
Success Count
Failure Count
Cancellation Count
Average Runtime

Audit Requirements
Every transition must generate an audit event.
Fields
Task ID
Old State
New State
Timestamp
Execution ID

Error Handling
Invalid Transition
↓
Raise InvalidStateTransitionError

Unknown State
↓
Raise RuntimeStateError

Future Compatibility
Supports
Approval Manager
Tool Execution
MCP
Multi-Agent
Agent Workflows
Knowledge Graph Tasks
without redesign.

Example Transition Flow
Task Created
CREATED
↓
Planning
PLANNING
↓
Execution
RUNNING
↓
Successful Completion
COMPLETED

Pseudocode
state_machine.transition(PLANNING)
↓
validate()
↓
update_state()
↓
emit_event()
↓
return_state()

Unit Test Requirements
Valid Transitions
Invalid Transitions
Terminal State Handling
State Inspection
Transition Validation
Coverage Target
100%

Acceptance Criteria
State machine implemented.
Valid transitions succeed.
Invalid transitions fail.
Terminal states enforced.
Unit tests passing.
Observability hooks defined.

Definition of Done
TaskStateMachine approved.
Ready for Runtime integration.
Ready for Completion Manager integration.
Ready for Event System integration.

