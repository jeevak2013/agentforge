Conversation Manager Design
Version: 1.0
Status: Approved
Last Updated: 2026-06-03

1. Purpose
The Conversation Manager is responsible for managing all runtime conversation history.
It ensures:
Efficient context usage
Context window protection
Message organization
Conversation summarization
Long-running task support
The Conversation Manager acts as the bridge between:
Runtime
and
Context Builder

2. Problem
Agent conversations continuously grow.
Example
User Message
↓
Tool Call
↓
Tool Result
↓
Observation
↓
Next Tool Call
↓
More Results
↓
More Messages
After hundreds of iterations, conversation history becomes too large for model context windows.

3. Architecture
Runtime
↓
Conversation Manager
↓
Context Builder
↓
Provider

4. Responsibilities
Store Messages
Manage History
Merge Messages
Compress History
Generate Summaries
Trim Context
Provide Context Views
Track Token Usage

5. Conversation Lifecycle
Message Created
↓
Stored
↓
Used In Context
↓
Compressed
↓
Summarized
↓
Archived

6. Conversation Components
Current Messages
Historical Messages
Conversation Summary
Tool History
System Messages
Runtime Events

7. Message Types
SYSTEM
USER
ASSISTANT
TOOL_CALL
TOOL_RESULT
OBSERVATION
SUMMARY
EVENT

8. Message Model
Fields
message_id
task_id
message_type
content
created_at
token_count
metadata

9. Storage Strategy
Active Messages
PostgreSQL
Redis Cache

Archived Messages
PostgreSQL
Future Object Storage

10. Conversation Window
Purpose
Maintain active context.

Contains
Recent Messages
Recent Tool Results
Current Plan
Recent Decisions

Older messages may be compressed.

11. Token Budget Management
Conversation Manager tracks:
Input Tokens
Output Tokens
Conversation Size
Summary Size

Used by:
Context Builder
Provider Layer
AgentOps

12. Message Merging
Problem
Many consecutive messages create noise.
Example
Tool Result
Tool Result
Tool Result
Tool Result

Solution
Merge Similar Messages
↓
Single Context Block

13. Compression Strategy
Purpose
Reduce token consumption.

Methods
Message Merging
Deduplication
Summary Replacement
Relevance Filtering

14. Summarization Strategy
Purpose
Preserve information while reducing size.

Flow
Old Messages
↓
Summarizer
↓
Conversation Summary
↓
Archive Original Messages

15. Summary Model
Fields
summary_id
task_id
summary_text
message_range
created_at

16. Trigger Conditions
Generate Summary When:
Message Count Threshold
Token Threshold
Runtime Threshold
Manual Trigger

17. Context Trimming
Purpose
Prevent context overflow.

Priority Order
Current Task
Current Plan
Recent Tool Results
Recent Messages
Summary Memory
Archived History

Lowest priority content removed first.

18. Conversation Views
Full View
All Messages

Runtime View
Active Messages Only

Provider View
Optimized Context Window

Audit View
Complete History

19. Runtime Integration
After Every Iteration
Runtime
↓
Conversation Manager
↓
Store Messages
↓
Evaluate Context Size

20. Memory Integration
Conversation Manager
↓
Memory Manager
↓
Summary Memory

Important summaries become memory records.

21. Context Builder Integration
Context Builder never reads raw conversation storage.
Instead:
Context Builder
↓
Conversation Manager
↓
Optimized Context

22. Tool Result Handling
Tool Results may be:
Stored
Merged
Summarized
Archived

Large outputs should be compressed.

23. Long Running Tasks
Supports:
Hundreds
Thousands
Potentially Millions
of conversation events.

Only relevant context remains active.

24. Multi-Agent Future
Phase 8
Shared Conversation
Agent Conversations
Agent Summaries
Cross-Agent Context

Architecture
Shared Conversation Store
↓
Agent Views
↓
Context Builder

25. Observability
Track
Message Count
Token Usage
Summary Count
Compression Ratio
Context Size

Used By
Observability
AgentOps

26. Audit Requirements
All original messages must remain recoverable.
Even if summarized.

Audit History
Must remain immutable.

27. Failure Handling
Summary Failure
↓
Keep Original Messages

Compression Failure
↓
Continue Execution

Conversation Corruption
↓
Restore From Storage

28. Future Enhancements
Semantic Conversation Search
Conversation Embeddings
Cross-Task Retrieval
Knowledge Graph Integration
Conversation Analytics

29. Design Principles
The Conversation Manager must remain:
Reliable
Token Efficient
Observable
Auditable
Provider Agnostic
Scalable
Enterprise Ready
The purpose of the Conversation Manager is not to store everything in context.
Its purpose is to ensure the right information is available to the agent at the right time.
