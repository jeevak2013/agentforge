docs/implementation/01_Repository_Setup.md
Repository Setup Specification
Version: 1.0
Status: Approved
Sprint: Sprint-01 Runtime Foundation

Purpose
This document defines the initial AgentForge repository structure.
The objective is to create a scalable foundation that supports:
Runtime Engine
Provider Layer
Tool Framework
Memory Layer
MCP
Knowledge Graph
Multi-Agent
AgentOps
without requiring major repository restructuring later.

Repository Structure
agentforge/
├── src/
│
│ ├── core/
│ │ ├── runtime/
│ │ ├── task/
│ │ ├── state/
│ │ ├── completion/
│ │ ├── events/
│ │ └── context/
│ │
│ ├── infrastructure/
│ │ ├── providers/
│ │ ├── persistence/
│ │ ├── observability/
│ │ ├── security/
│ │ └── mcp/
│ │
│ ├── shared/
│ │ ├── schemas/
│ │ ├── constants/
│ │ ├── exceptions/
│ │ └── utils/
│ │
│ └── api/
│
├── tests/
│ ├── unit/
│ ├── integration/
│ └── fixtures/
│
├── docs/
│
├── scripts/
│
├── .env.example
│
├── pyproject.toml
│
├── README.md
│
└── .gitignore

Technology Stack
Language
Python 3.12

Package Management
Poetry

Validation
Pydantic v2

Testing
Pytest

Linting
Ruff

Formatting
Ruff Format

Logging
Structlog

Initial Folder Responsibilities
core/
Business Logic
Must not depend on external providers.

infrastructure/
External Integrations
Providers
Databases
MCP
Observability

shared/
Reusable Components
Schemas
Utilities
Exceptions

api/
Future FastAPI Layer
Not required in Sprint-01

Sprint-01 Active Modules
Only the following modules may contain implementation code:
core/runtime
core/task
core/state
core/completion
core/events
infrastructure/providers
shared/schemas
tests

Sprint-01 File Targets
core/state/
runtime_state.py
state_machine.py

core/task/
task.py
task_manager.py

core/runtime/
agent_runtime.py
execution_context.py

core/completion/
completion_manager.py

core/events/
events.py
event_bus.py

infrastructure/providers/
base_provider.py
mock_provider.py
provider_models.py

Definition of Done
Repository created
Folder structure created
Poetry initialized
Pytest configured
Ruff configured
Git initialized
Ready for RuntimeState implementation

Next Implementation Artifact
After repository setup:
RuntimeState
Task
ExecutionContext
TaskStateMachine
Provider Models
BaseProvider
MockProvider
CompletionManager
AgentRuntime
EventBus
This sequence forms the first executable AgentForge Runtime.

