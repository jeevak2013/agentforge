docs/architecture/05_API_Architecture.md
AgentForge API Architecture
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

1. Purpose
This document defines the API architecture for AgentForge.
The API layer provides a secure, versioned, and scalable interface between external clients and the AgentForge platform.
The API is responsible for:
Task management
Agent interaction
Workspace management
Approvals
Monitoring
Administration
The API never contains agent logic.
All agent execution is delegated to the Runtime Layer.

2. Architectural Principles
Principle 1
Thin Controllers
Controllers should:
Validate requests
Invoke services
Return responses
Controllers must not contain business logic.

Principle 2
Version Everything
All APIs must be versioned.
Example:
/api/v1/tasks

Principle 3
API First
All platform functionality must be accessible through APIs.
Future clients:
Web UI
CLI
VS Code Extension
Slack Bot
Teams Bot
Mobile App
must use the same APIs.

Principle 4
Stateless APIs
The API layer remains stateless.
Runtime state is stored in:
PostgreSQL
Redis

3. High-Level Architecture
           Clients
                 │
 ┌───────────────┼───────────────┐

 ▼               ▼               ▼

Web UI CLI Integrations
                │

                 ▼

          API Gateway

                 │

                 ▼

         FastAPI Layer

                 │

                 ▼

           Services

                 │

                 ▼

         Runtime Layer


4. API Modules
api/
├── health/
├── tasks/
├── messages/
├── workspaces/
├── approvals/
├── providers/
├── metrics/
├── evaluations/
├── agents/
├── mcp/
└── admin/

5. Health APIs
Purpose:
Platform monitoring.

GET /api/v1/health
Response:
{
"status": "healthy"
}

GET /api/v1/health/detailed
Response:
{
"database":"healthy",
"redis":"healthy",
"provider":"healthy"
}

6. Task APIs
Core runtime entry point.

POST /api/v1/tasks
Purpose:
Create new task.
Request:
{
"objective": "Create FastAPI Calculator API"
}
Response:
{
"task_id":"task_001"
}

GET /api/v1/tasks/{task_id}
Purpose:
Retrieve task.

GET /api/v1/tasks
Purpose:
List tasks.

POST /api/v1/tasks/{task_id}/cancel
Purpose:
Cancel task.

POST /api/v1/tasks/{task_id}/pause
Purpose:
Pause task.

POST /api/v1/tasks/{task_id}/resume
Purpose:
Resume task.

7. Message APIs
Purpose:
Human-Agent communication.

POST /api/v1/tasks/{task_id}/messages
Request:
{
"message":"Add JWT authentication"
}

GET /api/v1/tasks/{task_id}/messages
Response:
Conversation history.

8. Streaming APIs
Purpose:
Real-time task updates.

GET /api/v1/tasks/{task_id}/stream
Technology:
Server-Sent Events (SSE)
Initial Version

Future:
WebSockets

Events
THINKING
TOOL_CALL
TOOL_RESULT
PLAN_UPDATE
COMPLETED
FAILED

9. Workspace APIs
Purpose:
Manage isolated workspaces.

POST /api/v1/workspaces
Create workspace.

GET /api/v1/workspaces/{workspace_id}
Retrieve workspace.

POST /api/v1/workspaces/{workspace_id}/upload
Upload files.

GET /api/v1/workspaces/{workspace_id}/files
List files.

10. Approval APIs
Purpose:
Human-in-the-loop workflows.

GET /api/v1/approvals
Pending approvals.

POST /api/v1/approvals/{approval_id}/approve
Approve action.

POST /api/v1/approvals/{approval_id}/reject
Reject action.

11. Provider APIs
Purpose:
Provider management.

GET /api/v1/providers
List providers.

GET /api/v1/providers/models
List available models.

GET /api/v1/providers/health
Provider health status.

12. Metrics APIs
Purpose:
AgentOps.

GET /api/v1/metrics
Platform metrics.

GET /api/v1/tasks/{task_id}/metrics
Task metrics.

GET /api/v1/reports/cost
Cost reports.

13. Evaluation APIs
Purpose:
Quality measurement.

POST /api/v1/evaluations
Run evaluation.

GET /api/v1/evaluations/{evaluation_id}
Evaluation results.

14. Agent APIs
Phase 8
Multi-Agent Runtime.

POST /api/v1/agents
Create agent.

GET /api/v1/agents
List agents.

GET /api/v1/agents/{agent_id}
Retrieve agent.

15. MCP APIs
Phase 9

GET /api/v1/mcp/servers
List servers.

POST /api/v1/mcp/servers
Register server.

GET /api/v1/mcp/tools
List tools.

16. Admin APIs
Administrative operations.

GET /api/v1/admin/system
System information.

GET /api/v1/admin/config
Configuration.

GET /api/v1/admin/audit
Audit logs.

17. Authentication Architecture
Phase 1
API Key Authentication.

Phase 2
JWT Authentication.

Phase 3
OAuth2.
SSO.
Azure AD.
Okta.

18. Authorization Model
Roles
ADMIN
ENGINEER
ANALYST
VIEWER

Permissions
Create Task
Execute Task
Approve Actions
View Metrics
Manage Providers
Manage MCP

19. Request Validation
All requests validated using:
Pydantic

Validation Areas
Schema
Required Fields
Types
Business Rules

20. Response Standard
Success
{
"success": true,
"data": {}
}

Failure
{
"success": false,
"error": {
"code":"TASK_NOT_FOUND",
"message":"Task not found"
}
}

21. Error Categories
VALIDATION_ERROR
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
NOT_FOUND
CONFLICT
PROVIDER_ERROR
TOOL_ERROR
SECURITY_ERROR
SYSTEM_ERROR

22. Service Boundaries
API Layer
Responsibilities:
Authentication
Validation
Routing

Runtime Layer
Responsibilities:
Execution
Planning
Tool orchestration

Provider Layer
Responsibilities:
Model communication

Memory Layer
Responsibilities:
Persistence
Retrieval

Security Layer
Responsibilities:
Enforcement
Approval
Auditing

23. Future API Evolution
Future Features:
GraphQL
WebSockets
gRPC
Event APIs
Agent Marketplace APIs
Workflow APIs

24. Design Principles
The AgentForge API must remain:
Versioned
Stateless
Secure
Observable
Scalable
Backward Compatible
Provider Agnostic
Domain Agnostic
All external interactions with AgentForge must occur through the API layer.

