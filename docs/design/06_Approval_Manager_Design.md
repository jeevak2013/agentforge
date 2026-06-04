# Approval Manager Design

Version: 1.0

Status: Approved

Last Updated: 2026-06-02

---

# 1. Purpose

The Approval Manager controls human-in-the-loop authorization for high-risk agent actions.

It ensures that potentially dangerous actions cannot be executed without appropriate approval.

The Approval Manager serves as a safety boundary between:

Agent Intent

and

Real World Action

---

# 2. Problem

Agents can perform actions that may:

Modify Files

Execute Commands

Access Sensitive Data

Call External Systems

Deploy Applications

Delete Resources

Not all actions should be executed automatically.

---

# 3. Architecture

Agent Runtime
↓
Tool Request
↓
Approval Manager
↓
Approved?
↓
Tool Executor

---

# 4. Responsibilities

Risk Assessment

Approval Routing

Approval Collection

Approval Tracking

Approval Auditing

Approval Expiration

Policy Enforcement

---

# 5. Approval Workflow

Tool Request
↓
Risk Evaluation
↓
Approval Decision
↓
Approved
or
Rejected
↓
Runtime Continues

---

# 6. Approval Types

AUTO_APPROVED

USER_APPROVAL

ADMIN_APPROVAL

MULTI_LEVEL_APPROVAL

---

# 7. Auto Approval

Purpose

Allow safe actions without interruption.

Examples

read_file

list_files

search_files

---

Default Risk

LOW

---

# 8. User Approval

Purpose

Require confirmation from task owner.

Examples

write_file

edit_file

create_directory

---

Default Risk

MEDIUM

---

# 9. Admin Approval

Purpose

Require elevated approval.

Examples

delete_database

production_configuration_change

credential_update

---

Default Risk

HIGH

---

# 10. Multi-Level Approval

Purpose

Support enterprise governance.

Example

Agent
↓
Manager Approval
↓
Security Approval
↓
Execution

---

# 11. Risk Levels

LOW

MEDIUM

HIGH

CRITICAL

---

# 12. Risk Classification Matrix

LOW

Read Operations

Examples

read_file

search_files

list_files

---

MEDIUM

Workspace Modifications

Examples

write_file

edit_file

rename_file

---

HIGH

System Operations

Examples

execute_command

database_update

external_api_calls

---

CRITICAL

Production Operations

Examples

deploy_application

delete_production_database

infrastructure_changes

---

# 13. Approval Policy Engine

Purpose

Determine approval requirements.

Inputs

Tool

Risk Level

User Role

Environment

Workspace

---

Output

Approval Decision

---

# 14. Approval Request Model

Fields

approval_id

task_id

tool_name

action

risk_level

status

requested_at

expires_at

approved_by

---

# 15. Approval Statuses

PENDING

APPROVED

REJECTED

EXPIRED

CANCELLED

---

# 16. Runtime State Integration

When approval required:

RUNNING
↓
WAITING_FOR_APPROVAL

---

After approval:

WAITING_FOR_APPROVAL
↓
RUNNING

---

After rejection:

WAITING_FOR_APPROVAL
↓
REJECTED_ACTION

---

# 17. Approval Expiration

Purpose

Prevent indefinite waiting.

Examples

15 Minutes

1 Hour

24 Hours

Configurable

---

# 18. Approval Context

User must see:

Action

Tool

Target Resource

Risk Level

Reason

Potential Impact

---

Example

Tool:
execute_command

Command:
docker deploy production

Risk:
CRITICAL

---

# 19. Audit Logging

Every approval event must be logged.

Examples

Approval Requested

Approval Granted

Approval Rejected

Approval Expired

---

Stored In

audit_logs

---

# 20. Metrics

Track

Approval Count

Approval Time

Approval Rate

Rejection Rate

Risk Distribution

---

Used By

Observability

AgentOps

Security

---

# 21. Policy Examples

Development Environment

execute_command

AUTO_APPROVE

---

Production Environment

execute_command

USER_APPROVAL

---

Production Deployment

deploy_application

ADMIN_APPROVAL

---

# 22. Multi-Agent Considerations

Future Phase

Planner Agent

Coder Agent

Reviewer Agent

Tester Agent

All approval requests pass through a centralized Approval Manager.

---

# 23. Emergency Stop

Purpose

Immediate interruption of execution.

Workflow

Operator
↓
Stop Task
↓
Approval Manager
↓
Runtime Halted

---

# 24. Security Integration

Integrated With

Security Manager

Policy Engine

Audit Logger

RBAC

---

# 25. Future Features

Policy-as-Code

Approval Delegation

Slack Approvals

Teams Approvals

Jira Approvals

Mobile Approvals

---

# 26. Design Principles

The Approval Manager must remain:

Secure

Auditable

Observable

Policy Driven

Environment Aware

Enterprise Ready

No high-risk action may bypass the Approval Manager.
