# Context Builder Design

Version: 1.0

Status: Approved

---

# Purpose

The Context Builder is responsible for constructing the final prompt sent to an LLM.

The Runtime never directly builds prompts.

Instead:

Runtime
↓
Context Builder
↓
Provider

---

# Problem

Agent context originates from many sources:

User Request

System Prompt

Memory

Plans

Tool Results

Workspace Information

Retrieved Knowledge

Model Limits

The Context Builder assembles these into a single optimized context.

---

# Responsibilities

Build System Prompt

Inject User Messages

Inject Memory

Inject Plans

Inject Tool Results

Inject Retrieved Knowledge

Manage Token Budget

Optimize Context Window

---

# Architecture

Runtime
↓
Context Builder
↓
Provider Request

---

# Inputs

Task

Conversation

Plan

Memory

Tool History

Workspace Metadata

Retrieved Documents

---

# Context Layers

Layer 1

System Instructions

---

Layer 2

Agent Role

---

Layer 3

Current Task

---

Layer 4

Plans

---

Layer 5

Conversation

---

Layer 6

Tool Results

---

Layer 7

Retrieved Memory

---

Layer 8

Retrieved Knowledge

---

# Token Budget Management

Problem

Context Window Limited

---

Solution

Rank Content

Summarize Content

Remove Low Value Content

Compress History

---

# Retrieval Integration

Context Builder receives:

Semantic Memory

Code Retrieval

Knowledge Retrieval

and injects only relevant results.

---

# Output

ProviderRequest

messages

tools

system_prompt

metadata

---

# Design Principles

Deterministic

Token Efficient

Memory Aware

Provider Agnostic

Observable
