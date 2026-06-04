docs/design/02_Provider_Design.md
AgentForge Provider Design
Version: 1.0
Status: Approved
Last Updated: 2026-06-02

1. Purpose
This document defines the provider abstraction architecture used by AgentForge.
The Provider Layer enables AgentForge to communicate with:
Cloud Models
OpenAI
Anthropic
Gemini
OpenRouter
Azure OpenAI
Local Models
Ollama
LM Studio
vLLM
OpenAI-Compatible APIs
without requiring runtime changes.

2. Design Goals
The Provider Layer must be:
Provider Agnostic
Extensible
Observable
Cost Aware
Streaming Capable
Enterprise Ready

3. Core Principle
Runtime Never Talks To Providers Directly
Bad:
Runtime
↓
OpenAI
Runtime
↓
Anthropic

Good:
Runtime
↓
ProviderManager
↓
Provider Interface
↓
Specific Provider

This isolates provider-specific logic.

4. High-Level Architecture
AgentRuntime
↓
ProviderManager
↓
BaseProvider
↓
Provider Implementation
Examples
OpenAIProvider
AnthropicProvider
GeminiProvider
OllamaProvider
vLLMProvider

5. Provider Responsibilities
Provider Layer owns:
Model Communication
Streaming
Retry Logic
Response Conversion
Token Tracking
Cost Tracking
Health Checks

Provider Layer does NOT own:
Planning
Tool Execution
Memory
Task State
Business Logic

6. Provider Manager
Purpose:
Central provider orchestration.
Responsibilities:
Provider Selection
Model Selection
Health Validation
Fallback Routing
Metrics Collection

Public Interface
get_provider()
list_models()
health_check()

7. Base Provider Interface
All providers must implement:
connect()
generate()
stream()
count_tokens()
health_check()

Future:
structured_output()
embeddings()
vision()
audio()

8. Standard Request Model
ProviderRequest
Fields
messages
system_prompt
tools
temperature
max_tokens
metadata

This becomes the canonical runtime request format.

9. Standard Response Model
ProviderResponse
Fields
content
tool_calls
usage
finish_reason
provider
model
latency

All providers must return this structure.

10. Message Translation Layer
Problem
Each provider expects different formats.
Example
OpenAI
messages[]

Anthropic
content blocks

Gemini
parts[]

Solution
Translation Layer
Runtime Format
↓
Provider Format
↓
Model

Runtime never sees provider-specific structures.

11. Tool Calling Architecture
Provider Support Matrix
OpenAI
✓ Tool Calling

Anthropic
✓ Tool Calling

Gemini
✓ Tool Calling

Ollama
Model Dependent

vLLM
Model Dependent

Provider Layer normalizes tool calls.

12. Streaming Architecture
Flow
Runtime
↓
Provider
↓
Model Stream
↓
Provider Stream Adapter
↓
Runtime

Benefits
Real-Time Updates
Lower Latency
Better UX

13. Structured Output Architecture
Future Requirement
Support:
Pydantic
JSON Schema
TypedDict

Flow
Runtime
↓
Schema
↓
Provider
↓
Validated Response

14. Token Tracking
Provider Layer tracks:
Input Tokens
Output Tokens
Total Tokens

Used by:
Metrics
AgentOps
Cost Analytics

15. Cost Tracking
Provider Layer calculates:
Request Cost
Task Cost
Run Cost

Example
Claude Sonnet
Input Cost
Output Cost
Total Cost

Stored in:
metrics

16. Retry Strategy
Failure Types
Rate Limit
Timeout
Network Failure
Temporary Provider Failure

Policy
Exponential Backoff

Example
Attempt 1
Attempt 2
Attempt 3
Fail

17. Fallback Strategy
Future Phase
Primary
Claude
↓
Failure
↓
GPT
↓
Failure
↓
Ollama

ProviderManager controls fallback logic.

18. Health Check Architecture
Each provider must expose:
health_check()

Checks
Authentication
Latency
Availability

Used by
Monitoring
Deployment Validation
AgentOps

19. OpenAI Provider
Responsibilities
Chat Completions
Tool Calls
Streaming
Embeddings
Future GPT Models

20. Anthropic Provider
Responsibilities
Messages API
Tool Use
Streaming
Future Claude Models

21. Gemini Provider
Responsibilities
Generate Content
Tool Use
Multimodal Support

22. OpenRouter Provider
Responsibilities
Unified access to multiple models.

Benefits
Model experimentation
Provider redundancy

23. Ollama Provider
Responsibilities
Local model execution.

Examples
Llama
Qwen
DeepSeek
Mistral

Benefits
Privacy
Low Cost
Offline Usage

24. LM Studio Provider
Responsibilities
Local desktop model execution.

Primary Usage
Development
Experimentation

25. vLLM Provider
Responsibilities
Enterprise local model serving.

Examples
GPU Clusters
Private Cloud Models
High Throughput Serving

26. Future LLM Gateway
Phase 9.5
Architecture
Runtime
↓
ProviderManager
↓
LLM Gateway
↓
Provider

Responsibilities
Routing
Cost Optimization
Fallbacks
Governance

27. Multi-Modal Roadmap
Future Support
Images
Documents
Audio
Video

Provider Capability Matrix maintained by ProviderManager.

28. Observability Integration
Metrics
Latency
Tokens
Cost
Failures

Traces
Provider Calls
Streaming Events
Retries

Logs
Request Metadata
Response Metadata

29. Security Considerations
Provider Layer must:
Protect API Keys
Mask Sensitive Data
Prevent Secret Leakage
Audit Provider Usage

Secrets stored in:
Environment Variables
Vault Systems
Future Secret Managers

30. Provider Selection Strategy
Version 1
Manual Selection

Version 2
Policy-Based Selection

Version 3
Automatic Routing
Based On
Cost
Latency
Quality
Task Type

31. Design Principles
The Provider Layer must remain:
Provider Agnostic
Extensible
Observable
Secure
Cost Aware
Local-LLM Friendly
Enterprise Ready
The Runtime must never depend on any provider-specific implementation.


