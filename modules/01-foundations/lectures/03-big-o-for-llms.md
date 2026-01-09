# Lecture 03: Big O for LLMs
**Cost, Speed, and the "Token Budget"**

---

## 📋 Lecture Overview

| Attribute | Value |
|-----------|-------|
| **Duration** | 8 minutes (Video) + 30 minutes (Lab) |
| **Core Concept** | Time complexity (Big O) applies to Model Selection (Cost/Latency). |
| **Prerequisites** | Basic Big O awareness. |
| **Learning Objectives** | Map models to complexity classes, understand token economics, optimize for latency. |

---

## 🎥 Concept Video Script (8 Minutes)

### The Three Tiers (0:00-2:00)
**Visual:** A pyramid. Bottom: "Haiku/Flash" (Fast, Cheap). Middle: "Sonnet/GPT-4o-mini" (Balanced). Top: "Opus/GPT-4" (Slow, Smart, Expensive).
**Narration:** "In CS, we have O(1) for instant lookups and O(n²) for heavy loops. In AI, we have the same tiers.
*   **O(1) Tasks:** Formatting, simple classification. Use Gemini Flash.
*   **O(n) Tasks:** Summarization, code generation. Use Claude Sonnet.
*   **O(n²) Tasks:** Complex reasoning, architecture design. Use GPT-4/Opus."

### The "Let's Just Use the Best Model" Trap (2:00-5:00)
**Visual:** A burning pile of money.
**Narration:** "Junior devs send *everything* to the smartest model. This is like using a supercomputer to add 2+2. It's slow (latency) and expensive (tokens). An Architect routes traffic. They use the 'cheapest model that works'."

### Latency is the New Bottleneck (5:00-8:00)
**Visual:** A loading spinner that never ends vs. a snappy UI.
**Narration:** "Users hate waiting. Gemini Flash responds in 0.5s. GPT-4 might take 5s. That 10x difference kills user experience. We will learn to 'chain' models: let the fast model handle the easy stuff, and only escalate to the smart model when necessary."

---

## 🧪 Lab 03: The Token Budget

### Scenario
You are building a "Receipt Scanner" app. You have a budget of $0.00 (Free Tier constraints). You need to process 1,000 receipts per day.

### Step 1: The Benchmark
**Task:**
1.  Take a sample receipt text.
2.  Prompt **Gemini Pro** (Free): "Extract the total amount." Measure time.
3.  Prompt **Claude Sonnet** (Free): "Extract the total amount." Measure time.
4.  Record the "Latency" for each.

### Step 2: The Stress Test
**Task:**
1.  Create a "complex" prompt: "Analyze this receipt, categorize every item, and suggest a diet plan."
2.  Run it on the fast model. Does it fail?
3.  Run it on the smart model. Does it work?
4.  **Architect's Decision:** Is the diet plan feature *worth* the extra latency/cost?

### Step 3: The Routing Logic
Write a pseudo-code function `route_task(task_type)`:
```python
def route_task(task):
    if task.is_simple_extraction:
        return use_gemini_flash(task) # O(1) cost
    elif task.is_complex_reasoning:
        return use_gpt4(task) # O(n^2) cost
```

---

## 🧠 Reflection
**Write 3 sentences:**
1.  Why is "using the best model" sometimes bad engineering?
2.  How does Latency impact the "feeling" of an AI app?
3.  If you had to pay for tokens yourself, how would your prompting change?
