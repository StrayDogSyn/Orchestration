# Code Review Prompt Template

Use this template when reviewing code for The AI Orchestrator project.

---

## Standard Review Prompt

```
Review this code following The AI Orchestrator standards:

**Correctness**:
1. Are there any bugs or logic errors?
2. Does it handle edge cases (None, empty, boundary values)?
3. Is error handling appropriate?

**Performance**:
4. What is the time complexity (Big O)?
5. What is the space complexity (Big O)?
6. Can it be optimized without sacrificing readability?

**Readability**:
7. Are variable/function names descriptive?
8. Is the code structure logical?
9. Are complex sections commented?

**Style Compliance**:
10. Does it follow PEP 8 (Python) or project JS standards?
11. Are type hints present (Python)?
12. Does it have proper docstrings?

**Project Fit**:
13. Works with free-tier tools only?
14. Teaches fundamentals (not just syntax)?
15. Accessible to target audience?

Provide specific, actionable feedback. No generic advice.
```

---

## Quick Review (Low-Priority Changes)

```
Quick code review:
- Spot any obvious bugs?
- Check Big O complexity
- Verify style compliance (Black, PEP 8)

Brief feedback only.
```

---

## Deep Review (Critical Code)

```
Deep review of this critical code:

**Security**:
- Any SQL injection risks?
- Proper input validation?
- Secrets properly managed?

**Architecture**:
- Is this the right approach?
- Are there better design patterns?
- How will this scale?

**Testing**:
- What edge cases need tests?
- Can this fail silently?
- How to validate correctness?

**Documentation**:
- Is the docstring complete?
- Are complex decisions explained?
- Is the API clear?

Thorough analysis required. Flag any concerns.
```

---

## Student Code Review (Educational)

```
Review this student code with pedagogical intent:

**What They Did Well**:
- Highlight correct patterns
- Note good decisions

**Learning Opportunities**:
- Where can they improve Big O?
- What patterns would be cleaner?
- How to handle errors better?

**Guided Questions** (don't give answers):
- "What happens if the input is None?"
- "How would you optimize this from O(n²) to O(n)?"
- "Can you explain why you chose this data structure?"

Be encouraging but rigorous. Foster growth mindset.
```

---

## Model-Specific Review

### For Gemini Flash (Fast Review)

```
Quick review focusing on:
1. Syntax errors
2. Obvious bugs
3. Style violations

Keep response under 200 words.
```

### For Claude Sonnet (Deep Analysis)

```
Comprehensive review:
1. Algorithm correctness
2. Performance analysis (Big O)
3. Edge case handling
4. Security implications
5. Architecture fit

Detailed feedback with examples.
```

### For GPT-4o-mini (Balanced)

```
Balanced review covering:
1. Bugs and logic errors
2. Performance (Big O)
3. Readability
4. Test suggestions

Moderate detail, actionable feedback.
```

---

## Follow-Up Prompts

### If Review Finds Issues

```
Based on your review, suggest specific refactoring:
1. Show "before" and "after" code
2. Explain why the change improves things
3. Note any tradeoffs
4. Provide tests for the fix
```

### If Review Is Positive

```
This code looks good. Suggest one advanced optimization:
- Could use a more efficient algorithm?
- Could leverage a design pattern?
- Could improve for large-scale data?

Only if meaningful improvement exists.
```

---

**Usage Notes**:
- Adjust depth based on code criticality
- For curriculum code, emphasize teaching over perfection
- For production code, prioritize security and performance
- Always explain rationale, not just what to change
