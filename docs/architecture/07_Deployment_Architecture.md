docs/architecture/07_Deployment_Architecture.md
AgentForge Deployment Architecture
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

1. Purpose
This document defines the deployment architecture for AgentForge.
It specifies:
Deployment environments
Infrastructure components
Containerization strategy
Scaling strategy
Local LLM deployment
Cloud deployment
Hybrid deployment
Disaster recovery
The deployment architecture ensures AgentForge can operate from a developer laptop to a large enterprise environment without requiring major architectural changes.

2. Deployment Principles
Principle 1
Container First
All services must run inside containers.
Technology:
Docker
Benefits:
Portability
Consistency
Simplified deployment

Principle 2
Cloud Agnostic
AgentForge must not depend on a specific cloud provider.
Supported:
AWS
Azure
GCP
On-Premise

Principle 3
Local LLM Support
Local models are first-class citizens.
Supported:
Ollama
LM Studio
vLLM
OpenAI-Compatible Endpoints
Cloud models remain optional.

Principle 4
API and Runtime Separation
API services must remain separate from long-running runtime execution.
This enables:
Horizontal scaling
Reliability
Better resource utilization

Principle 5
Infrastructure as Code
Infrastructure must be reproducible.
Technology:
Terraform

3. Deployment Modes
AgentForge supports four deployment modes.

Mode 1 — Local Development
Purpose:
Developer and research environments.
Architecture:
Developer Laptop
AgentForge API
AgentForge Worker
PostgreSQL
Redis
Qdrant
MinIO
Ollama
All services run locally.

Mode 2 — Team Environment
Purpose:
Small team deployments.
Architecture:
Shared VM or Server
AgentForge API
AgentForge Worker
PostgreSQL
Redis
Qdrant
MinIO
Optional:
Ollama
OpenAI
Anthropic

Mode 3 — Enterprise Production
Purpose:
Production deployments.
Technology:
Kubernetes
Architecture:
API Pods
Worker Pods
PostgreSQL
Redis
Qdrant
MinIO
Monitoring Stack
Ingress Controller

Mode 4 — Hybrid AI Deployment
Purpose:
Enterprise environments using private models.
Architecture:
AgentForge Platform
↓
LLM Gateway
↓
Private Model Infrastructure
Examples:
Ollama Cluster
vLLM Cluster
GPU Servers
Private Cloud Models

4. Local Development Architecture
Objective
Enable developers to start the platform with a single command.
Command:
docker compose up

Services
agentforge-api
Responsibilities:
FastAPI
API endpoints
Authentication

agentforge-worker
Responsibilities:
Runtime execution
Planning
Tool execution

postgres
Responsibilities:
Transactional storage

redis
Responsibilities:
Runtime state
Queues
Locks

qdrant
Responsibilities:
Embeddings
RAG

minio
Responsibilities:
Object storage

ollama
Responsibilities:
Local LLM execution

5. Local Deployment Diagram
Developer
↓
AgentForge API
↓
AgentForge Worker
↓
PostgreSQL
Redis
Qdrant
MinIO
↓
Ollama

6. Production Architecture
Objective
Support enterprise-grade deployments.
Architecture:
Internet
↓
Load Balancer
↓
Ingress
↓
AgentForge API Pods
↓
Redis Queue
↓
AgentForge Worker Pods
↓
PostgreSQL
Qdrant
MinIO
↓
Providers

7. API Service
Purpose:
Handle client requests.
Responsibilities:
Authentication
Validation
Task submission
Streaming
Must remain stateless.

8. Worker Service
Purpose:
Execute agent tasks.
Responsibilities:
Runtime loop
Tool execution
Planning
Memory updates
Workers consume tasks from queues.

9. Queue Architecture
Purpose
Decouple request handling from execution.
Workflow:
User Request
↓
API
↓
Task Queue
↓
Worker
↓
Runtime
↓
Completion

Initial Technology
Redis Queue

Future Options
RabbitMQ
Kafka

10. Storage Deployment
PostgreSQL
Stores:
Tasks
Messages
Plans
Metrics
Audit Logs
Characteristics:
Durable
Transactional

Redis
Stores:
Agent State
Execution Context
Queues
Locks
Characteristics:
Fast
Temporary

Qdrant
Stores:
Embeddings
Code Indexes
Retrieval Memory
Characteristics:
Semantic Search

MinIO
Stores:
Files
Artifacts
Reports
Snapshots
Characteristics:
S3-Compatible

11. Local LLM Architecture
Supported Local Providers
Ollama
LM Studio
vLLM
OpenAI-Compatible APIs

Provider Flow
Runtime
↓
Provider Layer
↓
Local Model
No runtime changes are required when switching providers.

12. Cloud LLM Architecture
Supported Providers:
OpenAI
Anthropic
Gemini
OpenRouter
Azure OpenAI
Flow:
Runtime
↓
Provider Layer
↓
Cloud Provider

13. Hybrid AI Architecture
Objective
Allow enterprises to keep models private.
Architecture:
AgentForge
↓
LLM Gateway
↓
Private GPU Cluster
Examples:
DeepSeek
Qwen
Llama
Mistral
Benefits:
Data Privacy
Cost Optimization
Regulatory Compliance

14. Kubernetes Architecture
Core Components:
agentforge-api Deployment
agentforge-worker Deployment
postgres StatefulSet
redis Deployment
qdrant StatefulSet
minio Deployment
ingress Controller
monitoring Stack

15. Scaling Strategy
API Scaling
Scale Horizontally
More API Pods

Worker Scaling
Scale Horizontally
More Worker Pods

Retrieval Scaling
Scale Qdrant Nodes

Storage Scaling
Use managed database services or clustered deployments.

16. Security Deployment
Security Components:
Authentication Layer
Authorization Layer
Approval Service
Audit Logging
Secrets Management

Future Integrations
OAuth2
Azure AD
Okta
Vault

17. Disaster Recovery
Backup Targets
PostgreSQL
Qdrant
MinIO

Backup Strategy
Daily Backup
Weekly Snapshot
Monthly Archive

Recovery Objective
Restore platform with minimal data loss.

18. CI/CD Architecture
Source Control:
GitHub

Pipeline:
Commit
↓
Build
↓
Test
↓
Security Scan
↓
Container Build
↓
Deployment

Future:
GitHub Actions
Azure DevOps
GitLab CI/CD

19. Cost Optimization Strategy
Model Routing
Simple Tasks
↓
Local Models
Complex Tasks
↓
Premium Models
Examples:
Claude
GPT
Gemini

Future
LLM Gateway-based intelligent routing.

20. Future Deployment Evolution
Version 1
Docker Compose

Version 2
Kubernetes

Version 3
Multi-Region Enterprise Deployment

Version 4
Agent Operating System Infrastructure

21. Design Principles
The AgentForge deployment architecture must remain:
Portable
Scalable
Cloud Agnostic
Provider Agnostic
Secure
Observable
Enterprise Ready
Local-LLM Friendly
The deployment architecture must support both local experimentation and enterprise-scale production deployments without requiring fundamental architectural changes.

