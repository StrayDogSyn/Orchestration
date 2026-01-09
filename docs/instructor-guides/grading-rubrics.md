# Consolidated Grading Rubrics

---

## 📦 Module 1: Foundations
**Project:** Personal Code Explainer

| Criterion | Weight | Novice (0-50%) | Competent (51-80%) | Architect (81-100%) |
| :--- | :--- | :--- | :--- | :--- |
| **Fundamentals** | 30% | Accepts AI output blindly. | Checks for syntax errors. | **Challenges AI's analysis.** Validates Big O. Catches edge cases. |
| **Orchestration** | 30% | Hard-coded string prompt. | Configurable prompt. | **Structured Prompt (JSON).** Chain-of-Thought logic used. |
| **Zero-Cost Ops** | 20% | Crashes on rate limit. | Basic try/except. | **Exponential Backoff.** Caching implemented. |
| **Code Quality** | 10% | Spaghetti code. | Functions used. | **Modular Design.** Separation of Concerns. |
| **Documentation** | 10% | No docs. | Basic README. | **Design Rationale.** Architecture Diagram. |

---

## 📦 Module 2: Prompting
**Project:** Smart Model Router

| Criterion | Weight | Novice | Competent | Architect |
| :--- | :--- | :--- | :--- | :--- |
| **Routing Logic** | 40% | Random routing. | Basic keyword match. | **Complexity Analysis.** Routes O(1) tasks to Flash, O(n²) to Pro. |
| **Cost Efficiency** | 30% | Uses expensive model. | Mixed usage. | **Minimizes Token Usage.** Stays under free tier limits. |
| **Evaluation** | 30% | No metrics. | Basic success/fail. | **Latency/Cost Benchmarks.** Data-driven decisions. |

---

## 📦 Module 3: Memory (RAG)
**Project:** Learning Flashcard System

| Criterion | Weight | Novice | Competent | Architect |
| :--- | :--- | :--- | :--- | :--- |
| **Retrieval** | 40% | Keyword search only. | Basic vector search. | **Hybrid Search (Keyword + Vector).** Re-ranking. |
| **Persistence** | 30% | In-memory only. | Local file save. | **Vector DB (Chroma/Pinecone).** Persistent storage. |
| **Accuracy** | 30% | Hallucinates answers. | Mostly correct. | **Source Citations.** "I don't know" fallback. |

---

## 📦 Module 4: Agents
**Project:** Capstone Platform

| Criterion | Weight | Novice | Competent | Architect |
| :--- | :--- | :--- | :--- | :--- |
| **Autonomy** | 40% | Human does everything. | Single step agent. | **Multi-step Reasoning.** Tool use (Search, Code Exec). |
| **Reliability** | 30% | Breaks often. | Works mostly. | **Self-Correction.** Error recovery loops. |
| **Architecture** | 30% | Monolithic script. | Basic classes. | **Micro-kernel Architecture.** Plugin system. |
