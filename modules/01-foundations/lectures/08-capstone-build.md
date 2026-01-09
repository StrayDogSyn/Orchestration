# Lecture 08: The Capstone Build
**Project Launch: Personal Code Explainer**

---

## 🚀 Mission Briefing

You have learned the theory. You have practiced the skills. Now, you build.

**Goal:** Create a tool that allows you to leverage AI to understand complex code, without blindly trusting it.

**Reference:** [Module 1 Capstone Design Document](../../../../module_1_capstone.md)

---

## 🛠️ The Build Process

### Day 1: The Skeleton
1.  **Setup:** Create your project folder, git repo, and virtual environment.
2.  **Config:** Create your `.env` file with your API key.
3.  **Core Class:** Implement `CodeArchitect` class (from Lab 07) that connects to the API.
4.  **Test:** Run a simple script to verify it can send "Hello" and get a response.

### Day 2: The Architect's Brain
1.  **Prompt Engineering:** Implement the structured prompt (Lecture 04) to get JSON output for Big O and Explanations.
2.  **Parsing:** Write code to parse the AI's response safely.
3.  **Resilience:** Add the retry logic (Lecture 06) to handle 429 errors.

### Day 3: The Interface & Audit
1.  **UI:** Build the CLI using `argparse` or `input()`.
2.  **Logging:** Implement the file saver to create your "Audit Log" markdown files.
3.  **Verification:** Run the tool on a snippet of code you *know* is O(n²). Does the AI agree?

---

## ✅ Submission Checklist

Before you mark Module 1 as "Complete", verify:

- [ ] **Code works:** I can run `python main.py my_script.py` and get an analysis.
- [ ] **Zero Cost:** It handles rate limits without crashing.
- [ ] **Verification:** I have 3 Audit Logs showing the tool in action.
- [ ] **Reflection:** I have written my 1-page Design Journal.

---

## 🏆 Graduation

Once you have pushed your code to GitHub and verified your features, you have graduated from **Module 1: Foundations**.

You are no longer just a coder. You are an **Architect**.

**Next Stop:** Module 2 - Prompt Engineering as Code.
