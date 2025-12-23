# Lab 01: Fix the AI's Homework

**Module**: 01 - Foundations  
**Lecture**: 01 - The Architect's Advantage  
**Duration**: ~28 minutes  
**Skills**: Complexity analysis, prompt engineering, code verification

---

## Objective

Learn to identify performance issues in AI-generated code and craft prompts that request both solutions AND explanations.

---

## What You'll Do

1. Analyze the time complexity of a list-based search function (O(n))
2. Identify the optimal data structure for O(1) lookups (dictionary/hash map)
3. Write an "architect's prompt" that gets the AI to explain its reasoning
4. Test both versions and compare performance
5. Reflect on your role as the "architect" vs the AI as the "implementer"

---

## Files

- `starter.md` - Main lab notebook (start here)
- `tracker_original.py` - The buggy code (for reference)
- `solution.py` - Instructor reference (don't peek until after!)

---

## Prerequisites

- Basic Python (lists, dictionaries, for loops)
- Understanding of O(n) vs O(1) complexity
- Access to ChatGPT or Claude (free tier is fine)

---

## How to Complete

### Option 1: Markdown (Recommended for Beta Test)
1. Open `starter.md` in a text editor
2. Read through and fill in answers directly in the file
3. Run code snippets in Python REPL or Jupyter

### Option 2: Google Colab (Full Experience)
1. Upload `starter.md` to Colab
2. Convert markdown cells to code cells as needed
3. Run inline tests

### Option 3: Local Python
1. Use `tracker_original.py` as base
2. Follow along with `starter.md` questions
3. Create `tracker_optimized.py` with your solution

---

## Success Criteria

You've completed the lab when:

- ✅ You can explain why the original code is O(n)
- ✅ You can articulate why a dictionary makes it O(1)
- ✅ Your "architect's prompt" requests explanation, not just code
- ✅ You tested both versions and saw measurable speedup
- ✅ You answered all three reflection questions thoughtfully

---

## Estimated Time

| Task | Time |
|------|------|
| Setup & Read | 3 min |
| Task 1-2: Analysis | 10 min |
| Task 3: Prompt Crafting | 10 min |
| Task 4-6: Testing | 8 min |
| Task 7: Reflection | 5 min |
| **Total** | **~35 min** |

*(Lecture estimates 28 min - we'll adjust based on beta testing)*

---

## Need Help?

**Stuck on complexity analysis?**
- Hint: Ask yourself "how many items does Python check in the worst case?"
- For O(n): Every item in the list
- For O(1): Direct lookup (like a phone book index)

**Stuck on the optimal data structure?**
- Think about how a real phone book works
- You don't scan every name - you jump to the right section
- What Python data structure works like that?

**AI gave you code but no explanation?**
- Your prompt might be too vague
- Try: "Explain step-by-step why [X] is better than [Y]"
- Don't accept "it's faster" - demand specifics!

---

**Created**: December 23, 2025  
**Status**: Beta Test Version  
**Next Update**: After Hunter's self-test feedback
