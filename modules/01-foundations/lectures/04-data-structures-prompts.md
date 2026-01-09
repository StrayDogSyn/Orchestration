# Lecture 04: Data Structures as Prompt Patterns
**Structuring Inputs for Better Reasoning**

---

## 📋 Lecture Overview

| Attribute | Value |
|-----------|-------|
| **Duration** | 7 minutes (Video) + 30 minutes (Lab) |
| **Core Concept** | Structuring data in prompts (JSON, Lists) improves AI reasoning. |
| **Prerequisites** | Arrays, Dictionaries/Hash Maps. |
| **Learning Objectives** | Use JSON for strict output, use Lists for instructions, Chain-of-Thought as Linked Lists. |

---

## 🎥 Concept Video Script (7 Minutes)

### The Paragraph Problem (0:00-2:00)
**Visual:** A wall of text vs. a bulleted list.
**Narration:** "LLMs get lost in paragraphs, just like humans. If you bury instructions in a block of text, the model might miss them. This is unstructured data. Architects love *structured* data."

### JSON: The Universal Language (2:00-4:30)
**Visual:** A JSON object with strict keys.
**Narration:** "Don't ask the AI to 'write a summary.' Ask it to 'return a JSON object with keys: `summary`, `sentiment`, and `tags`.' This forces the model into a rigid structure (a Hash Map). It reduces hallucinations because the model has a 'form' to fill out."

### Chain-of-Thought as Linked Lists (4:30-7:00)
**Visual:** A chain of nodes. Node 1 -> Node 2 -> Node 3.
**Narration:** "Complex logic fails if you jump to the answer. Force the AI to think in steps. Step 1 leads to Step 2. This is a Linked List of reasoning. If Node 1 is wrong, the whole chain breaks—which makes it easier to debug!"

---

## 🧪 Lab 04: Prompt Refactoring

### Scenario
You have a vague prompt that produces inconsistent results. You need to "refactor" it using data structures.

### Step 1: The Bad Prompt
**Prompt:**
> "Read this email and tell me if they are angry and what they want and maybe write a reply if it's important."

**Task:**
1.  Run this 3 times. Note the inconsistent formatting.

### Step 2: The JSON Refactor (Hash Map)
**Task:**
Rewrite the prompt to request this JSON schema:
```json
{
  "is_angry": boolean,
  "customer_intent": string,
  "requires_immediate_reply": boolean,
  "draft_reply": string (optional)
}
```
Run it. Note how much easier it is to parse programmatically.

### Step 3: The Step-by-Step Refactor (Linked List)
**Task:**
Add "Chain of Thought" instructions:
1.  "First, analyze the sentiment keywords."
2.  "Second, compare against our refund policy."
3.  "Third, decide if a reply is needed."
4.  "Finally, output the JSON."

---

## 🧠 Reflection
**Write 3 sentences:**
1.  How does JSON output make it easier to integrate AI into a Python script?
2.  Why does breaking a prompt into "steps" improve accuracy?
3.  Which data structure (List, Dict, Graph) best represents a conversation history?
