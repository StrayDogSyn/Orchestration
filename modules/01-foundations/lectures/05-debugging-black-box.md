# Lecture 05: Debugging the Black Box
**Fixing Code You Didn't Write**

---

## 📋 Lecture Overview

| Attribute | Value |
|-----------|-------|
| **Duration** | 6 minutes (Video) + 30 minutes (Lab) |
| **Core Concept** | You cannot step-debug an LLM, but you can debug the *input* and *output*. |
| **Prerequisites** | Python `print()` or `logging`. |
| **Learning Objectives** | Implement "Prompt Logging", isolate variables, understand Temperature/Non-determinism. |

---

## 🎥 Concept Video Script (6 Minutes)

### The Missing Stack Trace (0:00-2:00)
**Visual:** A classic Python stack trace vs. an LLM hallucination (no error, just wrong output).
**Narration:** "When Python fails, it gives you a stack trace. When an LLM fails, it gives you... a convincing lie. You can't step-debug the model's weights. You treat it as a **Black Box**. To debug a black box, you must control the inputs and measure the outputs."

### Prompt Logging: The Flight Recorder (2:00-4:00)
**Visual:** A log file showing: `[INPUT] -> [OUTPUT]`.
**Narration:** "Never run a prompt without saving it. If an AI generates buggy code, you need to know *exactly* what you sent it. Did you make a typo? Did you forget a constraint? Your prompts are your source code now. Version control them."

### Temperature & The Flaky Test (4:00-6:00)
**Visual:** A thermostat. Cold (0.0) = Deterministic. Hot (1.0) = Creative/Random.
**Narration:** "Code is deterministic. 2+2=4. AI is probabilistic. 2+2 might be '4' or 'Four' or 'IV'. This is controlled by **Temperature**. For code, keep it cool (0.0 - 0.2). For creative writing, heat it up. If your code works once but fails the next time, check your temperature."

---

## 🧪 Lab 05: The Flaky Test

### Scenario
You are building a "Color Hex Code Generator." You want the AI to return just the hex code (e.g., `#FF0000`).

### Step 1: The Determinism Check
**Task:**
1.  Set your API Temperature to `1.0` (High).
2.  Loop 5 times: Send the prompt "Give me the hex code for bright red."
3.  Print the exact output characters.
4.  **Observation:** You likely got variations: `#FF0000`, `The code is #FF0000`, `#ff0000`. This breaks your app.

### Step 2: Locking It Down
**Task:**
1.  Set Temperature to `0.0`.
2.  Run the loop 5 times.
3.  **Observation:** Outputs should be identical (or nearly so).

### Step 3: The System Prompt Fix
**Task:**
Refactor the prompt to use a System Instruction:
> "You are a color API. You output ONLY the hex string. No markdown, no explanations."

Run the loop again. Verify 100% success rate.

---

## 🧠 Reflection
**Write 3 sentences:**
1.  Why is "It worked on my machine" even more dangerous with AI?
2.  How does a System Prompt act like a "Type Signature" for the conversation?
3.  What happens if you try to generate creative poetry with Temperature 0.0?
