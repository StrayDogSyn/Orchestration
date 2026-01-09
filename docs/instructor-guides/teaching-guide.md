# Instructor Teaching Guide
**Philosophy & Facilitation**

---

## 🌟 The Core Philosophy
**"We are not teaching them to use AI. We are teaching them to ORCHESTRATE AI."**

Your job is not to lecture. Your job is to **Challenge**.
*   When a student shows you working code, ask: "Did you write this, or did the AI?"
*   If they say "The AI," ask: "Explain line 14 to me."
*   If they can't, it's not their code. It's the AI's code.

---

## 🎯 The "Chinese Room" Protocol
In every interaction, enforce the distinction between **Operator** and **Architect**.

### The Operator (Bad)
*   Pastes prompts blindly.
*   Accepts first result.
*   Says "It works" but can't debug edge cases.

### The Architect (Good)
*   Designs structured prompts.
*   Validates outputs.
*   Refactors code for efficiency (Big O).
*   Says "It works, and here are the trade-offs I made."

---

## 🛠️ Grading & Feedback

### The "Bug Hunt" Method
Don't just fix their code.
1.  **Spot the AI Bug:** Find a subtle error (or inefficiency) that AI tools commonly make (e.g., O(n²) lookups, hallucinated libraries).
2.  **Ask the Question:** "What happens if I pass a list of 1 million items to this function?"
3.  **Wait:** Let them realize the AI failed them.
4.  **Coach:** Guide them to the solution.

### The Zero-Cost Enforcer
Strictly enforce the free-tier mandate.
*   If a student says "I bought Copilot," tell them to turn it off.
*   They need to learn to build *without* paid crutches first.
*   They need to learn to manage API keys and rate limits manually.

---

## 🛑 Intervention Points
Watch for these red flags:
1.  **The Copy-Paste Velocity:** Student submits complex code way too fast.
    *   *Intervention:* Live code review. Ask them to modify the code on the fly.
2.  **The "It's Magic" Attitude:** Student treats the AI as a magic box.
    *   *Intervention:* Assign Lecture 05 (Debugging the Black Box) again.
3.  **Imposter Syndrome:** Student feels the AI is smarter than them.
    *   *Intervention:* Show them the "Chinese Mail Room" video again. Remind them: The AI has no intent. You provide the intent.
