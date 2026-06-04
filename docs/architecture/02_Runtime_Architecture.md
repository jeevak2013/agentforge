# AgentForge Runtime Architecture

Version: 1.0

Status: Approved

Last Updated: 2026-06-02

---

# 1. Purpose

This document defines the architecture of the AgentForge Runtime.

The runtime is the execution engine responsible for:

- Task lifecycle management
- Agent execution
- Tool orchestration
- Memory coordination
- Provider communication
- State management
- Completion validation

The runtime is domain-independent and serves all future agents.

---

# 2. Runtime Responsibilities

The runtime owns:

✓ Task Execution

✓ State Management

✓ Planning Coordination

✓ Tool Execution

✓ Memory Updates

✓ Provider Communication

✓ Completion Handling

✓ Metrics Collection

The runtime does NOT own:

✗ Domain Logic

✗ Prompt Definitions

✗ Tool Implementations

✗ Business Rules

---

# 3. Runtime Philosophy

The runtime follows a deterministic execution model.

The LLM provides decisions.

The runtime provides control.

The runtime never blindly trusts model outputs.

Every action is validated before execution.

---

# 4. Runtime Components

AgentRuntime

├── TaskManager

├── StateManager

├── PlannerManager

├── ToolExecutor

├── ProviderManager

├── MemoryManager

├── CompletionManager

└── MetricsCollector

---

# 5. AgentRuntime

The central orchestrator.

Responsibilities:

- Start task
- Execute loop
- Coordinate components
- Handle completion
- Handle failures

Public Interface:

run_task()

pause_task()

resume_task()

cancel_task()

---

# 6. TaskManager

Purpose:

Manage task lifecycle.

States:

CREATED

PLANNING

RUNNING

WAITING_FOR_TOOL

WAITING_FOR_HUMAN

FAILED

COMPLETED

Responsibilities:

- State transitions
- Status tracking
- Task persistence

---

# 7. StateManager

Purpose:

Manage AgentState.

Stores:

- Messages
- Plans
- Tool history
- Iteration count
- Runtime status

Responsibilities:

- Read state
- Update state
- Persist state

---

# 8. PlannerManager

Purpose:

Coordinate planning.

Responsibilities:

- Generate plans
- Update plans
- Track progress

Outputs:

Plan

Plan Steps

Task Breakdown

---

# 9. ProviderManager

Purpose:

Abstract model providers.

Responsibilities:

- Provider selection
- Model selection
- Streaming
- Retries
- Health checks

Supported Providers:

OpenAI

Anthropic

Gemini

OpenRouter

Ollama

LM Studio

vLLM

---

# 10. ToolExecutor

Purpose:

Execute tools safely.

Execution Flow:

Tool Request
↓
Validation
↓
Security Checks
↓
Execution
↓
Tool Result

Responsibilities:

- Tool lookup
- Parameter validation
- Security enforcement
- Execution

---

# 11. MemoryManager

Purpose:

Manage memory systems.

Memory Types:

Short-Term Memory

Summary Memory

Retrieval Memory

Future:

Knowledge Graph Memory

Responsibilities:

- Save memory
- Retrieve memory
- Summarize history

---

# 12. CompletionManager

Purpose:

Validate task completion.

Agent requests completion using:

attempt_completion

The runtime verifies:

- Plan complete
- No pending actions
- No critical failures

Only then:

Task = COMPLETED

---

# 13. MetricsCollector

Purpose:

Capture runtime metrics.

Metrics:

Execution Time

Iterations

Tool Calls

Token Usage

Cost

Success Rate

Failure Rate

These metrics feed AgentOps.

---

# 14. Core Runtime Objects

ExecutionContext

AgentState

Task

Message

ToolCall

ToolResult

Plan

PlanStep

These objects flow through the runtime.

---

# 15. ExecutionContext

Purpose:

Carry execution metadata.

Fields:

task_id

workspace_id

user_id

provider

model

start_time

current_iteration

ExecutionContext travels through every runtime component.

---

# 16. AgentState

Purpose:

Represent current task state.

Fields:

messages

tool_history

current_plan

todo_list

status

iteration_count

This object is the source of truth for execution.

---

# 17. Runtime Loop

Core Logic:

while not completed:

    think()

    execute_tool()

    observe()

    update_memory()

    continue()

This pattern is inspired by:

- Roo Code
- Claude Code
- OpenHands
- LangGraph workflows

---

# 18. Think Phase

Inputs:

Objective

Messages

Memory

Plan

Tool Results

Workspace Context

Output:

Response

Tool Call

Plan Update

Completion Request

---

# 19. Observe Phase

Input:

Tool Result

Responsibilities:

- Update state
- Update memory
- Update metrics

Observation is required before next reasoning cycle.

---

# 20. Runtime Limits

Safety Controls:

Max Iterations

Default: 50

Max Tool Calls

Default: 100

Max Runtime Duration

Default: 30 Minutes

These values are configurable.

---

# 21. Failure Handling

Failure Types:

Provider Failure

Tool Failure

Security Failure

Timeout

Unexpected Exception

Strategies:

Retry

Fallback

Human Escalation

Abort

---

# 22. Future Multi-Agent Runtime

Current:

Single Runtime
↓
Single Agent

Future:

Runtime
↓
Agent Orchestrator
↓
Planner
Coder
Reviewer
Tester

Shared Memory

Shared Plan

Shared Metrics

---

# 23. Runtime Sequence Summary

Task Created
↓
State Initialized
↓
Plan Generated
↓
Provider Call
↓
Tool Execution
↓
Observation
↓
Memory Update
↓
Completion Validation
↓
Task Complete

---

# 24. Design Principles

The runtime must be:

Deterministic

Observable

Secure

Provider-Agnostic

Domain-Agnostic

Extensible

Testable

These principles take precedence over implementation convenience.

