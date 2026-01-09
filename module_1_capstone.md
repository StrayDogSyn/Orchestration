# Module 1 Capstone: Personal Code Explainer
**Title:** The Architect's Lens
**Estimated Time:** 8-12 Hours
**Difficulty:** Intermediate (Foundations)

## 1. Problem Statement
You are a developer who constantly encounters complex, undocumented code snippets (legacy code, StackOverflow answers, or obfuscated logic). You need a tool that doesn't just "explain" the code, but **teaches** you the underlying concepts using the "Architect's Advantage" principles (Time Complexity, Memory Usage, potential bugs).

Generic AI explanations are often too high-level or hallucinate safety. You need a **verified** explanation engine.

## 2. Required Features (MVP)
The application must be a CLI (Command Line Interface) tool or simple Web App (Streamlit/gradio) that:

1.  **Input:** Accepts a code snippet (Python/JS) or a file path.
2.  **Architectural Analysis:** Uses an LLM (Gemini/Claude) to analyze:
    *   Time Complexity (Big O).
    *   Potential Edge Cases / Bugs.
    *   "The Chinese Room Test": Does the code rely on obscure syntax over clear logic?
3.  **Socratic Teaching:** Doesn't just give the answer; asks the user 1-2 verification questions to ensure *they* understand the code.
4.  **Zero-Cost Resilience:** Handles API rate limits gracefully (retries/backoff).
5.  **Audit Log:** Saves the Input, Prompt, and Output to a local Markdown file for review.

## 3. Tech Stack (Strict Zero-Cost)
*   **Language:** Python 3.10+
*   **AI Provider:** Google Gemini Pro (via `google-generativeai` library) OR Claude Sonnet (via API if available, else scrape/manual). *Recommendation: Gemini Pro Free Tier.*
*   **Interface:** `argparse` (CLI) or `rich` (TUI) or `streamlit` (Web).
*   **Environment:** Local VS Code + `.env` for keys.

## 4. Assessment Rubric

| Category | Novice (1pt) | Competent (2pts) | Proficient (3pts) | Architect (4pts) |
| :--- | :--- | :--- | :--- | :--- |
| **Orchestration** | Hard-coded prompt. | Configurable prompt. | "Chain of Thought" prompt structure. | System prompts + Role-based prompting + Error recovery. |
| **Fundamentals** | Accepts AI output blindly. | Checks for basic errors. | Validates Big O analysis. | Challenges AI's analysis; forces AI to justify complexity claims. |
| **Code Quality** | Spaghetti code in one file. | Functions used. | Classes/Modules used. | Type hinting, Docstrings, and Separation of Concerns. |
| **Zero-Cost Ops** | Crashes on API error. | Prints error message. | Basic retry logic. | Exponential backoff + caching to save tokens. |
| **Documentation** | README exists. | Setup instructions included. | Architecture diagram included. | "Design Rationale" document explaining *why* choices were made. |

## 5. Starter Code Structure
```python
# structure.py
class CodeArchitect:
    def __init__(self, api_key):
        self.client = configure_genai(api_key)
        
    def analyze_complexity(self, code_snippet):
        """
        Prompt engineering challenge:
        Force the AI to output ONLY Big O notation and 1 sentence justification.
        """
        pass

    def generate_socratic_questions(self, code_snippet):
        """
        Ask the user questions to test their understanding.
        """
        pass

    def save_audit_log(self, interaction_data):
        """
        Save to markdown for review.
        """
        pass
```

## 6. Deliverables
1.  **Source Code:** GitHub repository link.
2.  **Audit Logs:** 3 examples of the tool analyzing complex code (e.g., a recursive function, a regex pattern).
3.  **Design Journal:** A short reflection (1 page) on "Where the AI tried to trick me, and how I caught it."
