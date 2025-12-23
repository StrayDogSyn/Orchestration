# Module 01: Foundations

> Why fundamentals matter MORE with AI

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/clipboard-list.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Overview

| Attribute | Value |
|-----------|-------|
| Duration | Weeks 1-3 (3 weeks) |
| Prerequisites | OOP, Algorithms, Big O |
| Difficulty | Beginner-Intermediate |
| Assessment | Project-based |

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/target.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Learning Objectives

By the end of this module, you will be able to:

1. **Explain the Chinese Mail Room problem** and why understanding beats mimicking
2. **Apply Big O analysis** to model selection decisions
3. **Map data structures** to prompt engineering patterns
4. **Identify algorithm patterns** in LLM workflow design
5. **Debug AI outputs** using CS mental models
6. **Build a Code Explainer** that demonstrates prompt-as-function understanding

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/books.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Module Content

### Lectures

| # | Topic | Duration | Status |
|---|-------|----------|--------|
| 01 | The Chinese Mail Room | TBD | ⏳ |
| 02 | Big O for Model Selection | TBD | ⏳ |
| 03 | Data Structures → Prompt Patterns | TBD | ⏳ |
| 04 | Algorithm Patterns in LLM Workflows | TBD | ⏳ |
| 05 | Debugging AI with CS Mental Models | TBD | ⏳ |

### Labs

| # | Exercise | Focus | Status |
|---|----------|-------|--------|
| 01 | Big O Comparison | Model timing analysis | ⏳ |
| 02 | Tree to Chain-of-Thought | Data structure mapping | ⏳ |
| 03 | Divide and Conquer Prompts | Algorithm patterns | ⏳ |
| 04 | Prompt Debugging | Systematic troubleshooting | ⏳ |

### Project

**Code Explainer**

Build an application that:
- Takes code as input
- Explains it using a structured prompt
- Demonstrates prompt-as-function thinking
- Handles edge cases gracefully

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/tool.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Prerequisites Check

Before starting this module, ensure you're comfortable with:

- [ ] **OOP**: Classes, inheritance, polymorphism
- [ ] **Data Structures**: Arrays, trees, hash maps, graphs
- [ ] **Algorithms**: Sorting, searching, recursion
- [ ] **Big O**: Time and space complexity analysis
- [ ] **Python**: Basic syntax and functions

> <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/bulb.svg" width="14" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Not sure if you're ready? If you can implement a binary search tree and explain its O(log n) lookup time, you're good to go!

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/brain.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Key Concepts

### The Chinese Mail Room Problem

**The Question**: Can someone who doesn't understand Chinese successfully respond to Chinese letters by following a rule book?

**Why It Matters**: This is exactly what happens when developers use AI without understanding. They can *appear* competent while having no actual understanding—and that breaks down at the worst possible moment.

### Big O for Model Selection

| Complexity | Model Type | Use Case |
|------------|------------|----------|
| O(1) | Fast models (Haiku) | Simple tasks, high volume |
| O(n) | Standard models (Sonnet) | Complex reasoning |
| O(n²) | Premium models (Opus) | Research, analysis |

The time/quality tradeoff in model selection mirrors algorithmic complexity tradeoffs.

### Data Structures as Prompt Patterns

| Data Structure | Prompt Pattern |
|----------------|----------------|
| **List** | Sequential instructions |
| **Tree** | Chain-of-thought reasoning |
| **Graph** | Multi-agent coordination |
| **Hash Map** | Lookup tables in prompts |

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/folder.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Directory Structure

```
01-foundations/
├── README.md           # This file
├── lectures/           # Lecture content
├── labs/               # Hands-on exercises
├── projects/           # Assessment projects
└── resources/          # Supplementary materials
```

## <img src="https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/link.svg" width="20" style="filter: invert(28%) sepia(23%) saturate(1377%) hue-rotate(94deg) brightness(96%) contrast(88%);" /> Navigation

- → [Module 02: Prompt Engineering](../02-prompting/)
- [All Modules](../README.md)
- [Course README](../../README.md)
- Working Python scripts demonstrating core concepts
- Documentation of learning journey
