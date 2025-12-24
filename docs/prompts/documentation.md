# Documentation Prompt Template

Templates for generating documentation that meets The AI Orchestrator standards.

---

## Function/Method Documentation

```
Generate Google-style docstring for this function:

Requirements:
1. One-line summary (under 80 chars)
2. Detailed description (if non-trivial)
3. Time complexity (Big O)
4. Space complexity (Big O)
5. Args with types and descriptions
6. Returns with type and description
7. Raises (if applicable)
8. Example with expected output

Example format:
"""
Brief one-line description.

Longer explanation if needed. Describe the algorithm approach
and why it's better than alternatives.

Time Complexity: O(n)
Space Complexity: O(1)

Args:
    param_name: Description of parameter
    
Returns:
    Description of return value
    
Raises:
    ValueError: When input is invalid
    
Example:
    >>> function_name(input)
    expected_output
"""

No generic phrases. Be specific.
```

---

## Module Documentation

```
Generate module docstring following this structure:

"""
Module: {module_name}
Project: The AI Orchestrator

{Brief description of module's purpose}

This module provides:
- Key feature 1
- Key feature 2
- Key feature 3

Typical usage:
    from module_name import ClassName
    
    obj = ClassName(args)
    result = obj.method()

Copyright © 2025 Eric 'Hunter' Petross
StrayDog Syndications LLC | Second Story Initiative
Licensed under MIT License
"""

Include:
1. Module purpose
2. Key exports
3. Usage example
4. Dependencies (if any)
```

---

## README Generation

```
Generate README.md for this module/project:

# {Module Name}

> Brief tagline describing purpose

## Overview

| Attribute | Value |
|-----------|-------|
| Purpose | What does this solve? |
| Prerequisites | What must user know? |
| Difficulty | Beginner/Intermediate/Advanced |

## Key Features

- Feature 1 with brief explanation
- Feature 2 with brief explanation
- Feature 3 with brief explanation

## Quick Start

```python
# Minimal working example
from module import Class

result = Class().method()
print(result)  # Expected output
```

## API Reference

### ClassName

Brief description.

**Methods**:
- `method_name(args)` - What it does, returns

## Examples

### Example 1: Common Use Case

```python
# Code example
```

Expected output:
```
Output here
```

## Performance

- Time Complexity: O(?)
- Space Complexity: O(?)
- Benchmarks: X operations/second

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT © 2025 Eric 'Hunter' Petross

Requirements:
- No generic emojis
- Use tables for specifications
- Include code examples with output
- Explain Big O complexity
- Keep it scannable (headers, lists)
```

---

## Architecture Documentation

```
Document this architectural decision:

# Architecture Decision Record (ADR)

## Context

What problem are we solving?

## Decision

What did we decide to do?

## Alternatives Considered

1. **Option A**: Description
   - Pros: ...
   - Cons: ...
   
2. **Option B**: Description
   - Pros: ...
   - Cons: ...

## Rationale

Why did we choose this option?
- Reason 1
- Reason 2
- Reason 3

## Consequences

### Positive
- Benefit 1
- Benefit 2

### Negative
- Tradeoff 1
- Tradeoff 2

## Implementation Notes

Key considerations when implementing:
1. Point 1
2. Point 2

## Future Considerations

What might we revisit?
- Consideration 1
- Consideration 2

---

**Date**: YYYY-MM-DD
**Status**: Accepted / Proposed / Superseded
**Deciders**: Names
```

---

## API Documentation

```
Generate API documentation:

## Endpoint: /api/endpoint

**Method**: GET | POST | PUT | DELETE

**Description**: What does this endpoint do?

**Authentication**: Required | Optional | None

**Request**:

```json
{
  "param1": "type - description",
  "param2": "type - description"
}
```

**Response Success (200)**:

```json
{
  "result": "type - description",
  "metadata": {
    "count": "int",
    "timestamp": "string"
  }
}
```

**Response Error (4xx/5xx)**:

```json
{
  "error": "string - error message",
  "code": "string - error code"
}
```

**Example Request**:

```bash
curl -X POST https://api.example.com/endpoint \
  -H "Authorization: Bearer TOKEN" \
  -d '{"param1": "value"}'
```

**Example Response**:

```json
{
  "result": "success",
  "metadata": {"count": 42}
}
```

**Rate Limits**: X requests per minute

**Notes**:
- Important note 1
- Important note 2
```

---

## Tutorial Documentation

```
Write tutorial following this structure:

# Tutorial: {Task Name}

**Duration**: X minutes
**Difficulty**: Beginner | Intermediate | Advanced
**Prerequisites**: What must you know first?

## What You'll Learn

By the end of this tutorial, you'll be able to:
- Learning objective 1
- Learning objective 2
- Learning objective 3

## Setup

```bash
# Installation or setup commands
```

## Step 1: {First Step}

Brief explanation of what we're doing.

```python
# Code for this step
```

**Expected output**:
```
Output here
```

**Why this works**: Explanation of the concept.

## Step 2: {Second Step}

Continue pattern...

## Common Pitfalls

### Pitfall 1: {Issue}

**Problem**: What goes wrong
**Solution**: How to fix it

## Next Steps

- Where to go from here
- Related tutorials
- Advanced topics

## Full Code

```python
# Complete, working code
```

---

**Last Updated**: YYYY-MM-DD
**Tested On**: Python 3.11, etc.
```

---

## Inline Comment Guidelines

```
Add inline comments following these rules:

**DO Comment**:
- Complex algorithms (explain approach)
- Non-obvious optimizations (why this way?)
- Edge case handling (what breaks this?)
- Magic numbers (what does 86400 mean?)

**DON'T Comment**:
- Obvious code (x = x + 1)
- What the code does (if code is clear)
- Redundant docstrings

**Format**:
# Why this is needed or what it prevents
code_here

NOT:
# Increments x
x += 1  # Bad comment
```

---

**Usage**:
- Adjust verbosity based on audience
- For curriculum: err on side of over-explaining
- For internal code: assume expert reader
- Always explain "why" not just "what"
