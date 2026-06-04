docs/architecture/06_Repository_Architecture.md
AgentForge Repository Architecture
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

1. Purpose
This document defines the repository structure, module ownership, dependency rules, and architectural boundaries for AgentForge.
The goal is to ensure:
Scalability
Maintainability
Clear ownership
Separation of concerns
Long-term architectural consistency

2. Architecture Philosophy
AgentForge follows a:
Modular Monolith Architecture
Version 1
with a future migration path toward:
Service-Oriented Architecture
Version 3+

Why Modular Monolith?
Advantages:
Faster development
Easier debugging
Lower operational complexity
Strong architectural boundaries
Future extraction into microservices remains possible.

3. Repository Structure
agentforge/
├── apps/
├── core/
├── domains/
├── infrastructure/
├── security/
├── agentops/
├── evaluation/
├── shared/
├── tests/
├── deployment/
├── docs/
└── scripts/

4. apps/
Purpose:
System entry points.
Contains:
apps/
├── api/
├── cli/
└── worker/

api/
Responsibilities:
FastAPI
Request validation
Response formatting
Authentication
Must NOT contain:
Runtime logic
Tool execution
Provider logic

cli/
Future command-line interface.
Examples:
agentforge task create
agentforge task run

worker/
Background jobs.
Examples:
Long-running tasks
Scheduled jobs
Evaluation pipelines

5. core/
Purpose:
Heart of the platform.
Contains reusable runtime components.

Structure
core/
├── runtime/
├── planner/
├── orchestration/
├── memory/
└── state/

runtime/
Responsibilities:
Agent loop
Task execution
Lifecycle management
Equivalent to Roo's Task.ts concept.

planner/
Responsibilities:
Task decomposition
Plan generation
Todo management

orchestration/
Future:
Multi-agent coordination.
Agents:
Planner
Coder
Reviewer
Tester

memory/
Responsibilities:
Context management
Summaries
Retrieval

state/
Responsibilities:
AgentState
ExecutionContext
Runtime state

6. domains/
Purpose:
Business-domain logic.
This is the most important long-term architectural boundary.

Structure
domains/
├── coding/
├── data_science/
├── rcm/
├── transport/
└── research/

coding/
Contains:
Tools
Prompts
Evaluators
Workflows
specific to software development.

data_science/
Contains:
EDA
Feature Engineering
Training
Evaluation
specific tools and workflows.

rcm/
Contains:
Healthcare Revenue Cycle Management capabilities.
Examples:
Denial Analysis
Appeal Generation
Root Cause Analysis
Revenue Optimization

transport/
Contains:
Fleet Optimization
Route Planning
Capacity Management
Attendance Analytics

7. infrastructure/
Purpose:
External integrations.

Structure
infrastructure/
├── providers/
├── persistence/
├── vectorstores/
├── storage/
├── messaging/
└── mcp/

providers/
Contains:
OpenAI
Anthropic
Gemini
OpenRouter
Ollama
LM Studio
vLLM

persistence/
Contains:
PostgreSQL repositories
Redis repositories
Database migrations

vectorstores/
Contains:
Qdrant integration
Future:
Pinecone
Weaviate

storage/
Contains:
MinIO
Future:
AWS S3
Azure Blob

mcp/
Contains:
MCP clients
MCP server integrations
MCP adapters

8. security/
Purpose:
Security enforcement.

Structure
security/
├── approvals/
├── audit/
├── policies/
├── sandbox/
└── guardrails/

Responsibilities:
Workspace Security
Command Security
Prompt Security
Approval Workflows
Audit Logging

9. agentops/
Purpose:
Operational intelligence.

Structure
agentops/
├── metrics/
├── tracing/
├── monitoring/
└── reporting/

Responsibilities:
Cost Tracking
Token Tracking
Success Rates
Performance Monitoring

10. evaluation/
Purpose:
Measure quality.

Structure
evaluation/
├── coding/
├── rcm/
├── ds/
└── common/

Responsibilities:
Benchmarking
Scoring
LLM-as-a-Judge
Evaluation Pipelines

11. shared/
Purpose:
Reusable platform-wide components.

Structure
shared/
├── schemas/
├── constants/
├── exceptions/
├── utils/
└── types/

Rules:
No domain logic allowed.

12. tests/
Purpose:
Automated validation.

Structure
tests/
├── unit/
├── integration/
├── e2e/
└── performance/

Testing Pyramid
Unit Tests
↓
Integration Tests
↓
End-to-End Tests

13. deployment/
Purpose:
Deployment artifacts.

Structure
deployment/
├── docker/
├── kubernetes/
├── terraform/
└── helm/

Responsibilities:
Local Development
Cloud Deployment
Infrastructure Automation

14. docs/
Purpose:
Project knowledge base.

Structure
docs/
├── charter/
├── architecture/
├── design/
├── adr/
├── sprints/
├── knowledge/
├── operations/
└── research/

15. scripts/
Purpose:
Developer productivity.
Examples:
Database initialization
Seed data
Migration utilities
Benchmark scripts

16. Dependency Rules
Allowed Direction
apps
↓
core
↓
infrastructure

domains
↓
core

security
↓
shared

Forbidden
core → apps
core → domains
shared → infrastructure
domains → apps

17. Ownership Model
core/
Platform Team

domains/
Domain Teams

infrastructure/
Platform Team

security/
Security Team

agentops/
Operations Team

18. Repository Evolution
Version 1
Single Repository
Modular Monolith

Version 2
Multi-Agent Expansion

Version 3
Selective Service Extraction
Examples:
AgentOps Service
Evaluation Service
MCP Service

19. Architectural Principles
The repository must remain:
Modular
Testable
Observable
Secure
Provider-Agnostic
Domain-Agnostic
Extensible
No component may violate the dependency rules defined in this document.
Repository structure is considered part of the architecture and must evolve through ADRs.

