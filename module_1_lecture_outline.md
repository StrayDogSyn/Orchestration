# Module 1 Lecture Series Outline
**Theme:** Foundations - The Architect's Advantage
**Format:** Micro-Mastery (6min Video + Quiz + 30min Lab + Reflection)

---

## Lecture 1: The Architect's Advantage
*   **Status:** Existing (See `modules/01-foundations/lectures/01-architects-advantage.md`)
*   **Core Concept:** The "Chinese Room" thought experiment applied to coding.
*   **Lab:** "Fix the AI's Homework" - Optimizing O(n²) AI code.

---

## Lecture 2: The Chinese Mail Room (Deep Dive)
*   **Duration:** 6 minutes
*   **Core Concept:** AI has no understanding; it matches patterns. You provide the understanding.
*   **Prerequisites:** Lecture 1
*   **Student Will Learn:**
    1.  Why LLMs fail at logic puzzles but excel at syntax.
    2.  How to spot "hallucinated confidence."
    3.  The "Operator vs. Architect" mindset shift.
*   **Lab Exercise:** "The Hallucination Trap" - Students prompt an LLM with a trick question about a non-existent library method and must identify the hallucination.
*   **Connection:** Sets up the need for verification (Lecture 6).

---

## Lecture 3: Big O for LLMs (Cost & Speed)
*   **Duration:** 8 minutes
*   **Core Concept:** Time complexity (Big O) applies to Model Selection (Cost/Latency).
*   **Prerequisites:** Basic Big O awareness.
*   **Student Will Learn:**
    1.  Mapping models to complexity: Haiku (~O(1)), Sonnet (~O(n)), Opus (~O(n²)).
    2.  Token economics: Why "let's just use the best model" is bad engineering.
    3.  Latency trade-offs in real-time apps.
*   **Lab Exercise:** "The Token Budget" - Given a $0 budget, design a workflow for processing 1000 files. Compare cost of GPT-4 vs. Gemini Flash.
*   **Connection:** Crucial for the Capstone's model selection requirement.

---

## Lecture 4: Data Structures as Prompt Patterns
*   **Duration:** 7 minutes
*   **Core Concept:** Structuring data in prompts improves AI reasoning.
*   **Prerequisites:** Arrays, Dictionaries/Hash Maps.
*   **Student Will Learn:**
    1.  Why Bullet Lists (Arrays) are better than paragraphs for instructions.
    2.  Using JSON (Hash Maps) for strict output formatting.
    3.  Chain-of-Thought (Linked Lists) for sequential reasoning.
*   **Lab Exercise:** "Prompt Refactoring" - Take a vague paragraph prompt and refactor it into structured JSON-in/JSON-out specifications.
*   **Connection:** Enhances the quality of the Capstone's output.

---

## Lecture 5: Debugging the Black Box
*   **Duration:** 6 minutes
*   **Core Concept:** You cannot step-debug an LLM, but you can debug the *input* and *output*.
*   **Prerequisites:** Python print/logging.
*   **Student Will Learn:**
    1.  "Prompt Logging": The importance of saving the exact prompt sent.
    2.  Isolating variables: Changing one word at a time.
    3.  The "Temperature" variable and non-determinism.
*   **Lab Exercise:** "The Flaky Test" - Run the same prompt 10 times with Temp 1.0 vs Temp 0.1. Analyze variance.
*   **Connection:** Necessary for stable Capstone performance.

---

## Lecture 6: Zero-Cost Ops (The Free Tier Survival Guide)
*   **Duration:** 6 minutes
*   **Core Concept:** Engineering within constraints breeds creativity.
*   **Prerequisites:** API Key concepts.
*   **Student Will Learn:**
    1.  Rate Limits: Handling 429 Errors gracefully.
    2.  Environment Variables: `.env` security (never commit keys!).
    3.  Free Tier Strategy: Rotating keys vs. exponential backoff.
*   **Lab Exercise:** "Rate Limit Resilience" - Write a Python script that hits a dummy API limit and waits/retries automatically.
*   **Connection:** Essential for the "Zero-Cost" mandate of the project.

---

## Lecture 7: Architecting the Capstone
*   **Duration:** 5 minutes
*   **Core Concept:** Putting it all together into a cohesive system.
*   **Prerequisites:** Lectures 1-6.
*   **Student Will Learn:**
    1.  System Design: Flowcharting the "Code Explainer."
    2.  Separation of Concerns: UI vs. Logic vs. AI Service.
    3.  The MVP Mindset: What to build first.
*   **Lab Exercise:** "Blueprint Day" - Draw the architecture diagram for the Capstone. Define inputs and outputs.
*   **Connection:** Direct lead-in to the final build.

---

## Lecture 8: The Capstone Build
*   **Duration:** N/A (Project Launch)
*   **Core Concept:** Execution.
*   **Student Will Learn:** Integration of all previous skills.
*   **Lab Exercise:** The "Personal Code Explainer" Project (8-12 hours).
