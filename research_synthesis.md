# Research Synthesis: The AI Orchestrator Curriculum
**Date:** 2026-01-09
**Sources:** Gemini Pro (Pedagogy/Technical), Perplexity Pro (Market/Tools)
**Context:** Synthesis of findings for the "AI Orchestrator" bootcamp targeting justice-impacted developers.

## 1. Pedagogical Recommendations
The research confirms that traditional bootcamp models must be adapted for justice-impacted learners. Key strategies include:

*   **Micro-Mastery & "Small Wins":** Breaking complex topics into small, verifiable chunks (e.g., 6-minute concept videos + immediate quiz) builds confidence and combats imposter syndrome.
*   **The "Chinese Room Architect" Framework:** A recurring mental model where the student is the "architect" and the AI is the "operator." This prevents dependency and emphasizes the value of fundamentals.
*   **Organic Evolution (Co-Learning):** The most effective learning model is "teaching the AI." Students learn domain expertise by having to validate AI outputs and "teach" the model to improve.
*   **Project-Based Assessment (No Exams):** "Working code is the only credential." Assessment must verify *understanding*, not just functionality, by requiring students to explain *why* their code works and to debug AI-generated errors.
*   **Spaced Repetition:** Using the "Learning Flashcard System" project to reinforce concepts over time, leveraging the very memory systems (RAG) they are building.

## 2. Validated Free-Tier Tech Stack
To strictly adhere to the **Zero-Cost Mandate**, the following tools have been validated as viable for the entire curriculum:

| Category | Tool | Free Tier Limits | Use Case |
| :--- | :--- | :--- | :--- |
| **LLM (Primary)** | **Google Gemini Pro** | 60 req/min | Main "Architect" partner; broad reasoning. |
| **LLM (Secondary)** | **Claude Sonnet** | Daily limits (via claude.ai) | Code generation; "Chinese Room" operator. |
| **LLM (Fallback)** | **GPT-4o-mini** | Free tier available | Comparison testing; load balancing. |
| **Compute** | **Google Colab** | Free GPU access (T4) | Running Python notebooks; model testing. |
| **Vector DB** | **ChromaDB** | Unlimited (Local) | Persistent memory; RAG implementation. |
| **Vector DB (Cloud)**| **Pinecone** | 1 Index (Starter) | Cloud deployment experience. |
| **IDE** | **VS Code / Cursor** | Free | Development environment. |
| **Deployment** | **GitHub Pages** | Unlimited | Static site portfolio. |
| **Deployment** | **Vercel** | Hobby Tier | Dynamic app deployment. |

## 3. Contradictions & Resolutions
*   **Broad vs. Focused Scope:** Initial research (V1) suggested a general "AI Bootcamp" approach. However, data on justice-impacted learners (V2) strongly indicated a need for specialized "Second Chance" focus. **Resolution:** Adopted V2 "Justice-Focused" scope.
*   **Speed vs. Understanding:** AI tools prioritize speed (code generation), but the curriculum requires understanding (fundamentals). **Resolution:** The "Chinese Mail Room" analogy was adopted to explicitly devalue speed and revalue architectural control.
*   **Tool Volatility:** "Free tiers" change frequently. **Resolution:** The curriculum must feature "Graceful Degradation" strategies (e.g., if Pinecone becomes paid, fallback to local ChromaDB) as a core learning objective.

## 4. Pacing & Structure
*   **Duration:** 17-24 Weeks (Self-Paced).
*   **Structure:** 6 Modules.
    *   **Phase 1 (Weeks 1-6):** Foundations & Prompting (The "Why" and "How").
    *   **Phase 2 (Weeks 7-12):** Orchestration & Memory (System Design).
    *   **Phase 3 (Weeks 13-15):** Agents (Advanced Workflows).
    *   **Phase 4 (Weeks 16-24):** Capstone (Personal Platform).
*   **Checkpointing:** Strict gates at the end of each module to prevent "skipping ahead" without mastery.

## 5. Actionable Insights for Module 1
*   **Lecture 1 Focus:** Immediately introduce "The Architect's Advantage" to frame the student's role.
*   **Lab Design:** Labs must *force* the student to find bugs in AI code. "Fix the AI's homework" is a powerful pedagogical pattern.
*   **Capstone:** The "Personal Code Explainer" is the ideal Module 1 project as it requires *reading* code (fundamentals) and *prompting* AI (orchestration).
