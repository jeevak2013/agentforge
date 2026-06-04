# AgentForge System Architecture

Version: 1.0

Status: Approved

Last Updated: 2026-06-02

---

# 1. Purpose

This document defines the high-level architecture of AgentForge.

It describes:

- Major system components
- Responsibilities
- Component interactions
- Technology choices
- Architectural principles

This document serves as the foundation for all detailed design and implementation activities.

---

# 2. System Overview

AgentForge is an enterprise-grade AI Agent Platform.

The platform enables organizations to build, deploy, operate, and govern intelligent agents across multiple business domains.

Supported domains include:

- Coding
- Data Science
- Healthcare RCM
- Transport Operations
- Research

AgentForge provides a reusable runtime that powers all agents.

---

# 3. Architectural Principles

## Principle 1

Provider Independence

The runtime must never depend on a specific LLM vendor.

---

## Principle 2

Domain Independence

The runtime must support multiple domains without redesign.

---

## Principle 3

Security First

Security controls must be enforced by the platform rather than prompts.

---

## Principle 4

Observability By Default

Every significant action must be measurable and traceable.

---

## Principle 5

Extensibility

New tools, providers, and domains should be added without modifying the core runtime.

---

# 4. System Context

External Users

- Engineers
- Analysts
- Operators

External Systems

- OpenAI
- Anthropic
- Ollama
- GitHub
- Jira
- Slack
- Databases
- MCP Servers

AgentForge acts as the orchestration layer between users and intelligent agent execution.

---

# 5. High-Level Architecture

                Users
                   │
                   ▼
        ┌───────────────────┐
        │   API Layer       │
        └───────────────────┘
                   │
                   ▼
        ┌───────────────────┐
        │ Agent Runtime     │
        └───────────────────┘
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼

 Planner      Memory      Tool Executor

      ▼            ▼            ▼

 Providers   Storage     Security

      ▼
 Local & Cloud LLMs

---

# 6. Major Components

## API Layer

Responsibilities:

- Authentication
- Task Management
- Streaming
- Approvals
- Metrics Access

Technology:

- FastAPI

---

## Agent Runtime

Responsibilities:

- Task Lifecycle
- Agent Loop
- State Management
- Tool Coordination

Core Loop:

Think
↓
Tool Call
↓
Observe
↓
Memory Update
↓
Continue

---

## Planner

Responsibilities:

- Task Decomposition
- Todo Management
- Plan Tracking

Future:

Multi-agent planning workflows.

---

## Tool Executor

Responsibilities:

- Tool Discovery
- Validation
- Execution
- Result Handling

---

## Memory Layer

Responsibilities:

- Conversation History
- Summaries
- Retrieval Context
- Knowledge Storage

---

## Security Layer

Responsibilities:

- Workspace Isolation
- Command Policies
- Audit Logging
- Human Approval

---

## Provider Layer

Responsibilities:

- Model Communication
- Streaming
- Health Checks
- Routing

Supported Providers:

Cloud:

- OpenAI
- Anthropic
- Gemini
- OpenRouter

Local:

- Ollama
- LM Studio
- vLLM

---

# 7. Storage Architecture

## PostgreSQL

Stores:

- Tasks
- Messages
- Plans
- Metrics
- Audit Logs

---

## Redis

Stores:

- Active State
- Queues
- Locks

---

## Qdrant

Stores:

- Embeddings
- Semantic Memory
- Code Indexes

---

## MinIO

Stores:

- Artifacts
- Uploaded Files
- Generated Outputs

---

# 8. Runtime Execution Flow

User Request
↓
Task Creation
↓
Planning
↓
Provider Call
↓
Tool Execution
↓
Memory Update
↓
Completion
↓
Metrics Collection

Detailed execution flows are defined in:

docs/design/Runtime_Sequence_Diagrams.md

---

# 9. Domain Architecture

AgentForge separates runtime from domain logic.

Runtime Components:

- Runtime
- Providers
- Memory
- Security
- Storage

Domain Components:

- Tools
- Prompts
- Evaluators
- Workflows

Example Domains:

coding/
data_science/
rcm/
transport/

---

# 10. Deployment Architecture

Local Development:

Docker Compose

Production:

Kubernetes

Cloud:

AWS
Azure
GCP

Hybrid:

Cloud Infrastructure + Local Models

---

# 11. Future Evolution

Version 1

Single-Agent Coding Platform

---

Version 2

Multi-Agent Coding Platform

Agents:

- Planner
- Coder
- Reviewer
- Tester

---

Version 3

Enterprise Agent Platform

Multiple business domains.

---

Version 4

Agent Operating System

Enterprise-wide AI orchestration platform.

---

# 12. Success Criteria

The architecture is successful when:

- New agents can be created without runtime changes.
- New providers can be added without modifying runtime code.
- Multiple domains share the same platform.
- Local and cloud models are interchangeable.
- Enterprise deployment requirements are supported.

