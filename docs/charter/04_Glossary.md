docs/charter/04_Glossary.md
AgentForge Glossary
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

Purpose
This document establishes the official terminology used throughout AgentForge.
All architecture documents, ADRs, sprint plans, code, and discussions should use these definitions consistently.

A
Agent
An autonomous software entity capable of reasoning, planning, using tools, interacting with memory, and executing tasks.
Examples:
Coding Agent
Data Science Agent
RCM Agent
Planner Agent
Reviewer Agent
An agent is not the runtime.
An agent executes within the runtime.

AgentOps
The discipline of monitoring, evaluating, operating, and governing AI agents in production.
Examples:
Cost tracking
Monitoring
Tracing
Evaluation
Performance analysis

Agent Runtime
The execution engine responsible for managing agent lifecycles.
Responsibilities:
Task execution
State management
Tool execution
Provider communication
Completion handling
The runtime is the foundation of AgentForge.

C
Completion
The successful conclusion of a task.
A task is completed only when:
Objectives are satisfied
No pending tool executions remain
Runtime validation succeeds
Completion is not determined solely by the LLM.

Context
Information provided to the model during inference.
Examples:
User requests
Memory
Plans
Tool results
Retrieved documents

D
Domain
A business area supported by AgentForge.
Examples:
Coding
Data Science
Healthcare RCM
Transport
Research
Domains share the same runtime.
Only tools, prompts, workflows, and evaluations differ.

E
Evaluation
The process of measuring agent performance.
Examples:
Success rate
Accuracy
Code quality
Revenue impact
Evaluation is distinct from monitoring.

Execution Context
Runtime object containing information required during task execution.
Examples:
Task ID
User ID
Workspace ID
Provider
Model

G
Guardrail
A safety mechanism preventing unsafe agent behavior.
Examples:
Command restrictions
Prompt injection protection
Human approval requirements

L
LLM
Large Language Model.
Examples:
GPT
Claude
Gemini
DeepSeek
Qwen
Llama

LLM Gateway
A routing layer responsible for:
Model selection
Failover
Cost optimization
Governance

M
Memory
Stored information available to an agent.
Types:
Short-Term Memory
Current conversation and task history.

Summary Memory
Compressed history of previous interactions.

Retrieval Memory
Knowledge retrieved from vector databases.

MCP
Model Context Protocol.
A standard protocol enabling agents to discover and use external tools and resources.
Examples:
GitHub MCP
Jira MCP
Slack MCP
Database MCP

Multi-Agent System
A system where multiple specialized agents collaborate to solve objectives.
Examples:
Planner Agent
Coder Agent
Reviewer Agent
Tester Agent

P
Planner
Component responsible for:
Task decomposition
Plan generation
Progress tracking

Provider
An abstraction representing a model source.
Examples:
OpenAI
Anthropic
Gemini
Ollama
LM Studio
vLLM
The runtime communicates with providers rather than specific models.

R
RAG
Retrieval-Augmented Generation.
A technique that retrieves relevant information before model inference.
Pipeline:
Documents
↓
Embedding
↓
Retrieval
↓
LLM

Runtime Loop
The core execution cycle.
Think
↓
Tool Call
↓
Observe
↓
Memory Update
↓
Continue

S
State
The current condition of a running task.
Examples:
Messages
Plan
Tool history
Iteration count

Structured Output
Model output conforming to a predefined schema.
Typically implemented using:
Pydantic
JSON Schema
TypedDict

T
Task
A unit of work assigned to an agent.
Examples:
Create FastAPI API
Analyze denial data
Optimize transport routes
A task may contain multiple subtasks.

Tool
A capability available to an agent.
Examples:
read_file
write_file
search_files
execute_command
Tools allow agents to interact with external systems.

Tool Call
A request made by an agent to execute a tool.
Example:
{
"tool":"read_file",
"path":"main.py"
}

Tool Result
The outcome of a tool execution.
Example:
{
"success":true,
"output":"File content..."
}

V
Vector Database
Database optimized for storing and retrieving embeddings.
Examples:
Qdrant
Pinecone
Weaviate
Used primarily for RAG.

W
Workspace
An isolated environment assigned to a task.
Purpose:
Security
File management
Command execution
Agents operate only within their assigned workspace.

Workspace Manager
Component responsible for:
Workspace creation
Path validation
File operations
Isolation enforcement

Official Terminology Rule
All future documentation, ADRs, sprint plans, architecture diagrams, and implementation artifacts must use the definitions established in this glossary.
Changes to terminology require formal review and approval.
docs/charter/04_Glossary.md
AgentForge Glossary
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

Purpose
This document establishes the official terminology used throughout AgentForge.
All architecture documents, ADRs, sprint plans, code, and discussions should use these definitions consistently.

A
Agent
An autonomous software entity capable of reasoning, planning, using tools, interacting with memory, and executing tasks.
Examples:
Coding Agent
Data Science Agent
RCM Agent
Planner Agent
Reviewer Agent
An agent is not the runtime.
An agent executes within the runtime.

AgentOps
The discipline of monitoring, evaluating, operating, and governing AI agents in production.
Examples:
Cost tracking
Monitoring
Tracing
Evaluation
Performance analysis

Agent Runtime
The execution engine responsible for managing agent lifecycles.
Responsibilities:
Task execution
State management
Tool execution
Provider communication
Completion handling
The runtime is the foundation of AgentForge.

C
Completion
The successful conclusion of a task.
A task is completed only when:
Objectives are satisfied
No pending tool executions remain
Runtime validation succeeds
Completion is not determined solely by the LLM.

Context
Information provided to the model during inference.
Examples:
User requests
Memory
Plans
Tool results
Retrieved documents

D
Domain
A business area supported by AgentForge.
Examples:
Coding
Data Science
Healthcare RCM
Transport
Research
Domains share the same runtime.
Only tools, prompts, workflows, and evaluations differ.

E
Evaluation
The process of measuring agent performance.
Examples:
Success rate
Accuracy
Code quality
Revenue impact
Evaluation is distinct from monitoring.

Execution Context
Runtime object containing information required during task execution.
Examples:
Task ID
User ID
Workspace ID
Provider
Model

G
Guardrail
A safety mechanism preventing unsafe agent behavior.
Examples:
Command restrictions
Prompt injection protection
Human approval requirements

L
LLM
Large Language Model.
Examples:
GPT
Claude
Gemini
DeepSeek
Qwen
Llama

LLM Gateway
A routing layer responsible for:
Model selection
Failover
Cost optimization
Governance

M
Memory
Stored information available to an agent.
Types:
Short-Term Memory
Current conversation and task history.

Summary Memory
Compressed history of previous interactions.

Retrieval Memory
Knowledge retrieved from vector databases.

MCP
Model Context Protocol.
A standard protocol enabling agents to discover and use external tools and resources.
Examples:
GitHub MCP
Jira MCP
Slack MCP
Database MCP

Multi-Agent System
A system where multiple specialized agents collaborate to solve objectives.
Examples:
Planner Agent
Coder Agent
Reviewer Agent
Tester Agent

P
Planner
Component responsible for:
Task decomposition
Plan generation
Progress tracking

Provider
An abstraction representing a model source.
Examples:
OpenAI
Anthropic
Gemini
Ollama
LM Studio
vLLM
The runtime communicates with providers rather than specific models.

R
RAG
Retrieval-Augmented Generation.
A technique that retrieves relevant information before model inference.
Pipeline:
Documents
↓
Embedding
↓
Retrieval
↓
LLM

Runtime Loop
The core execution cycle.
Think
↓
Tool Call
↓
Observe
↓
Memory Update
↓
Continue

S
State
The current condition of a running task.
Examples:
Messages
Plan
Tool history
Iteration count

Structured Output
Model output conforming to a predefined schema.
Typically implemented using:
Pydantic
JSON Schema
TypedDict

T
Task
A unit of work assigned to an agent.
Examples:
Create FastAPI API
Analyze denial data
Optimize transport routes
A task may contain multiple subtasks.

Tool
A capability available to an agent.
Examples:
read_file
write_file
search_files
execute_command
Tools allow agents to interact with external systems.

Tool Call
A request made by an agent to execute a tool.
Example:
{
"tool":"read_file",
"path":"main.py"
}

Tool Result
The outcome of a tool execution.
Example:
{
"success":true,
"output":"File content..."
}

V
Vector Database
Database optimized for storing and retrieving embeddings.
Examples:
Qdrant
Pinecone
Weaviate
Used primarily for RAG.

W
Workspace
An isolated environment assigned to a task.
Purpose:
Security
File management
Command execution
Agents operate only within their assigned workspace.

Workspace Manager
Component responsible for:
Workspace creation
Path validation
File operations
Isolation enforcement

Official Terminology Rule
All future documentation, ADRs, sprint plans, architecture diagrams, and implementation artifacts must use the definitions established in this glossary.
Changes to terminology require formal review and approval.

