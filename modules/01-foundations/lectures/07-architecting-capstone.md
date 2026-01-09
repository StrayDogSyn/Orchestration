# Lecture 07: Architecting the Capstone
**From Blueprint to Build**

---

## 📋 Lecture Overview

| Attribute | Value |
|-----------|-------|
| **Duration** | 5 minutes (Video) + 30 minutes (Lab) |
| **Core Concept** | System Design and Separation of Concerns. |
| **Prerequisites** | Lectures 1-6. |
| **Learning Objectives** | Diagram the system, separate UI from Logic, define MVP features. |

---

## 🎥 Concept Video Script (5 Minutes)

### The Napkin Sketch (0:00-2:00)
**Visual:** Drawing boxes and arrows on a napkin. User -> UI -> Controller -> AI Service.
**Narration:** "Before you write a line of code, you draw. We are building the 'Personal Code Explainer'. What are the moving parts? We need a way to get input (UI). We need a brain to process it (AI Service). We need a memory to save it (File System)."

### Separation of Concerns (2:00-3:30)
**Visual:** A messy plate of spaghetti vs. a bento box.
**Narration:** "Don't put your API calls inside your UI code. If you switch from CLI to Web later, you'll have to rewrite everything. Keep your 'AI Logic' in one file (`architect.py`) and your 'Interface' in another (`main.py`). This is the Bento Box method."

### The MVP Mindset (3:30-5:00)
**Visual:** A skateboard vs. a car. Both get you from A to B.
**Narration:** "Don't build the Ferrari first. Build the skateboard.
*   **Version 1:** CLI tool. One hard-coded prompt. Prints to console.
*   **Version 2:** Add User Input. Add Error Handling.
*   **Version 3:** Add File Saving.
*   **Version 4:** Web UI.
Start with V1. Get it working. Then iterate."

---

## 🧪 Lab 07: Blueprint Day

### Scenario
You are the Lead Architect for the Capstone Project. You need to produce the technical spec.

### Step 1: The Flowchart
**Task:**
Draw a diagram (Excalidraw or Pencil/Paper) showing:
1.  **User Input:** Code Snippet.
2.  **Validator:** Check if input is empty.
3.  **AI Service:** Send to Gemini (with Retry Logic).
4.  **Parser:** Extract Big O and Explanations.
5.  **Output:** Display to user + Save to file.

### Step 2: The Interface Design
**Task:**
Define your Python Class signatures (Input/Output only, no code).
```python
class CodeArchitect:
    def analyze(self, code: str) -> dict:
        """Returns {'complexity': str, 'explanation': str}"""
        pass

class AuditLogger:
    def save(self, data: dict):
        """Appends to markdown file"""
        pass
```

### Step 3: The Prompt Draft
**Task:**
Write V1 of your System Prompt.
> "You are a Senior Software Architect. Analyze the following code for Time Complexity..."

Test this prompt manually in the web UI of Gemini/Claude to see if it works.

---

## 🧠 Reflection
**Write 3 sentences:**
1.  Why is it dangerous to start coding without a diagram?
2.  How does separating `CodeArchitect` from `main.py` make testing easier?
3.  What is the one "Must Have" feature for your MVP?
