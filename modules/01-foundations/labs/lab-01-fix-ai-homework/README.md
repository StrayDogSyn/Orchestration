# Lab 01: Fix the AI's Homework

## Overview

This hands-on lab accompanies
[Lecture 01: The Architect's Advantage][lecture].

**Duration**: ~28 minutes
**Difficulty**: Beginner-Intermediate
**Prerequisites**: Basic Python, OOP concepts, Big O awareness

---

## 🎯 Learning Objectives

By completing this lab, you will:

1. Analyze AI-generated code for performance issues (not just correctness)
2. Practice writing "architect-level" prompts that extract explanations
3. Verify AI suggestions through empirical testing
4. Experience the difference between *using* AI and *orchestrating* AI

---

## 📁 Lab Files

| File | Description |
|------|-------------|
| `starter.ipynb` | The lab notebook—work through this |
| `solution.ipynb` | Instructor reference (don't peek until done!) |
| `test_tracker.py` | Automated verification tests |

---

## 🚀 Getting Started

### Option A: Google Colab (Recommended)

1. Upload `starter.ipynb` to [Google Colab][colab]
2. Work through each cell in order
3. No installation required!

### Option B: Local Jupyter

```bash
# From the lab directory
jupyter notebook starter.ipynb
```

### Option C: VS Code

1. Open `starter.ipynb` in VS Code
2. Select a Python kernel
3. Run cells with Shift+Enter

---

## 📋 Lab Structure

| Task | Time | Description |
|------|------|-------------|
| **Task 1** | 5 min | Analyze the time complexity of AI-generated code |
| **Task 2** | 5 min | Diagnose the architectural issue |
| **Task 3** | 10 min | Write an architect's prompt and get AI response |
| **Task 4** | 8 min | Verify the fix with performance tests |

---

## ✅ Completion Criteria

You've completed this lab when you can:

- [ ] Explain why the original `find_by_company()` is O(n)
- [ ] Describe the trade-off of using a dictionary vs list
- [ ] Show an architect-level prompt you wrote
- [ ] Demonstrate measurable performance improvement in your tests

---

## 🆘 Stuck?

1. **Re-read the lecture** - especially the Chinese Room section
2. **Check the hints** - collapsible hints are embedded in the notebook
3. **Ask an AI** - but write an *architect's prompt*, not "help me"!
4. **Review the solution** - `solution.ipynb` (last resort)

---

## 📚 Related Resources

- [Big O Cheat Sheet][bigo]
- [Python Time Complexity][pytc]
- [Hash Tables Explained][hash]

---

**Next**: Complete the reflection questions in [Lecture 01][lecture],
then proceed to Lecture 02.

<!-- Link references -->
[lecture]: ../../lectures/01-architects-advantage.md
[colab]: https://colab.research.google.com/
[bigo]: https://www.bigocheatsheet.com/
[pytc]: https://wiki.python.org/moin/TimeComplexity
[hash]: https://www.youtube.com/watch?v=shs0KM3wKv8
