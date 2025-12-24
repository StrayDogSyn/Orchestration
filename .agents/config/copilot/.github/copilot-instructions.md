# GitHub Copilot Instructions

## Project: The AI Orchestrator

**Context**: Educational bootcamp for justice-impacted developers learning AI-augmented engineering.

**Target Audience**: Students with CS fundamentals (OOP, algorithms, Big O) learning to orchestrate LLMs as collaborative tools.

---

## Code Standards

### Python
- PEP 8 compliance (Black formatting, line length 88)
- Type hints required for all function signatures
- Google-style docstrings with complexity analysis
- Naming: `snake_case` functions, `PascalCase` classes

### JavaScript
- Modern ES6+ syntax
- Functional style preferred
- Const/let (never var)
- JSDoc for complex functions

### Documentation
- No generic emojis
- Use SVG icons for visual elements
- Explain "why" not just "what"
- Code examples must include expected output

---

## Never Suggest

- ❌ Paid tools (zero-cost mandate)
- ❌ Complex frameworks when simple solutions exist
- ❌ Generic boilerplate without context
- ❌ Code that bypasses fundamentals (e.g., using library when point is to learn algorithm)
- ❌ Placeholder comments like "TODO: implement"
- ❌ Solutions without Big O complexity analysis

---

## Always Include

- ✅ Type hints (Python) or JSDoc (JavaScript)
- ✅ Docstrings with time/space complexity
- ✅ Error handling for external calls
- ✅ Edge case handling (None, empty, boundary values)
- ✅ Example usage with expected output
- ✅ Explanation of algorithm choice

---

## Pedagogical Approach

When generating curriculum content:
1. Start with learning objectives
2. Explain the "why" (motivation)
3. Use analogies from cooking/gaming/90s movies (sparingly)
4. Show "before" and "after" code
5. Include hands-on exercise
6. Define assessment criteria

---

## Branding

- Project: "The AI Orchestrator" (capitalized, with "The")
- Copyright: "© 2025 Eric 'Hunter' Petross | StrayDog Syndications LLC"
- License: MIT

---

## Examples

### Good Code Generation

```python
def find_duplicates(arr: list[int]) -> list[int]:
    """
    Find duplicate integers using set-based approach.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        arr: List of integers
        
    Returns:
        Sorted list of duplicates
        
    Example:
        >>> find_duplicates([1, 2, 3, 2, 1])
        [1, 2]
    """
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return sorted(list(duplicates))
```

### Bad Code Generation

```python
# ❌ No docstring, no type hints, generic name
def process(data):
    result = []
    for item in data:
        if item in result:
            pass
        else:
            result.append(item)
    return result
```

---

**Note**: Continue.dev is the primary AI assistant. Use Copilot as fallback or alternative perspective.
