# Deployment Guide
**Sharing Your Portfolio with the World**

Your code means nothing if it stays on your laptop. This guide covers how to deploy your projects for **$0**.

---

## 🌍 Option 1: GitHub (The Standard)
**Best for:** Storing code, sharing your portfolio.

### 1. Push Your Code
Don't just upload files. Use Git.
```bash
git init
git add .
git commit -m "Initial commit of AI Orchestrator Portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-orchestrator.git
git push -u origin main
```

### 2. The README
Your README is your landing page. It must answer:
*   **What is this?** (A Personal AI Agent Platform)
*   **How do I run it?** (Setup steps)
*   **What makes it special?** (Zero-Cost architecture, RAG memory)

---

## 🌐 Option 2: GitHub Pages (The Portfolio Site)
**Best for:** Documentation and static demos.

1.  Go to your Repo Settings -> Pages.
2.  Select `main` branch -> `/root` folder.
3.  Click Save.
4.  Your site is live at `https://YOUR_USERNAME.github.io/ai-orchestrator/`.

**Tip:** Use this to host your **Design Journals** and **Audit Logs** as a blog.

---

## ⚡ Option 3: Vercel (The Web App)
**Best for:** Running Python/JS apps in the cloud (if you built a web UI).

1.  Sign up at [vercel.com](https://vercel.com) (Free Hobby Tier).
2.  Install CLI: `npm i -g vercel`
3.  Run `vercel` in your project folder.
4.  **Environment Variables:**
    *   Vercel will ask for your Environment Variables.
    *   Add `GEMINI_API_KEY` in the Vercel Dashboard (Settings -> Environment Variables).
    *   **NEVER** commit your `.env` file to Git.

---

## 📦 Option 4: Python Package (PyPI)
**Best for:** Making your CLI tool installable via `pip`.

1.  Structure your project with `setup.py`.
2.  Build: `python setup.py sdist bdist_wheel`
3.  Upload to TestPyPI first to verify.

---

## 🛑 Zero-Cost Deployment Checklist
Before you share your link:
*   [ ] **No Keys in Code:** Search for "sk-" or "API_KEY" in your code.
*   [ ] **Rate Limits:** Ensure your code handles 429 errors (so it doesn't crash during a demo).
*   [ ] **Readme:** Does it explain how to get a free API key?
