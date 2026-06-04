# docs/implementation/07_BaseProvider.md

# BaseProvider Specification

Version: 1.0

Status: Approved

Sprint: Sprint-01 Runtime Foundation

Related ADR

ADR-002 Provider Abstraction

---

# Purpose

BaseProvider defines the contract that every LLM provider must implement.

Examples

OpenAIProvider

AnthropicProvider

GeminiProvider

OllamaProvider

OpenRouterProvider

MockProvider

---

# Design Goals

Provider Agnostic

Extensible

Testable

Observable

Streaming Compatible

Tool Compatible

Multimodal Ready

---

# Architecture

AgentRuntime
↓
BaseProvider
↓
Concrete Provider

Examples

OpenAI

Anthropic

Ollama

---

# Dependency Rule

AgentRuntime

MUST depend on

BaseProvider

---

AgentRuntime

MUST NOT depend on

OpenAI SDK

Anthropic SDK

Ollama SDK

Provider-specific types

---

# Interface Definition

BaseProvider

Responsibilities

Generate Responses

Stream Responses

Health Checking

Token Counting

Provider Metadata

---

# Core Methods

generate()

stream()

health_check()

count_tokens()

provider_name()

---

# generate()

Purpose

Generate a complete response.

Input

ProviderRequest

Output

ProviderResponse

---

Example

Runtime
↓
generate()
↓
ProviderResponse

---

# stream()

Purpose

Generate streaming responses.

Input

ProviderRequest

Output

Iterator[ProviderChunk]

---

Future Sprint

Streaming support

---

# health_check()

Purpose

Verify provider availability.

Output

ProviderHealth

---

Used By

Provider Manager

Observability

AgentOps

---

# count_tokens()

Purpose

Estimate token usage.

Input

ProviderRequest

Output

TokenCount

---

Used By

Context Builder

Cost Estimation

Runtime Controls

---

# provider_name()

Purpose

Identify provider.

Output

String

Examples

OpenAI

Anthropic

Ollama

MockProvider

---

# Example Interface

class BaseProvider(ABC):

```
@abstractmethod
def generate(
    self,
    request: ProviderRequest
) -> ProviderResponse:
    pass

@abstractmethod
def stream(
    self,
    request: ProviderRequest
):
    pass

@abstractmethod
def health_check(
    self
) -> ProviderHealth:
    pass

@abstractmethod
def count_tokens(
    self,
    request: ProviderRequest
) -> int:
    pass

@abstractmethod
def provider_name(
    self
) -> str:
    pass
```

---

# Runtime Usage

ExecutionContext
↓
ProviderRequest
↓
BaseProvider.generate()
↓
ProviderResponse
↓
Runtime

---

# Error Handling

ProviderTimeoutError

ProviderAuthenticationError

ProviderRateLimitError

ProviderUnavailableError

ProviderValidationError

---

All provider-specific exceptions must be converted to AgentForge exceptions.

---

# Observability Requirements

Track

Provider Calls

Latency

Failures

Retries

Token Usage

Cost

---

Metrics

Requests Per Minute

Average Latency

Failure Rate

Provider Availability

---

# Security Requirements

No API Keys stored in Runtime.

Providers access credentials through configuration layer.

---

Provider implementations must never expose secrets in logs.

---

# Future Compatibility

Supports

Tool Calling

Structured Outputs

Multimodal Inputs

Reasoning Models

Streaming

MCP

Agent Collaboration

without interface redesign.

---

# Example Implementations

Sprint-01

MockProvider

---

Sprint-02

OpenAIProvider

AnthropicProvider

OllamaProvider

ProviderManager

---

# Unit Test Requirements

Generate Response

Health Check

Token Counting

Error Handling

Provider Metadata

Coverage Target

90%

---

# Acceptance Criteria

BaseProvider interface implemented.

Abstract methods defined.

Runtime dependency established.

No provider-specific dependencies in Runtime.

Unit tests passing.

---

# Definition of Done

BaseProvider approved.

Ready for MockProvider implementation.

Ready for OpenAI implementation.

Ready for Anthropic implementation.

Ready for Ollama implementation.

Provider abstraction successfully enforced.
