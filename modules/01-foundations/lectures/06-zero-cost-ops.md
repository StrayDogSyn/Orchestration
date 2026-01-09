# Lecture 06: Zero-Cost Ops
**The Free Tier Survival Guide**

---

## 📋 Lecture Overview

| Attribute | Value |
|-----------|-------|
| **Duration** | 6 minutes (Video) + 30 minutes (Lab) |
| **Core Concept** | Engineering within constraints breeds creativity. |
| **Prerequisites** | API Key concepts, Basic Python. |
| **Learning Objectives** | Handle Rate Limits (429), Secure API Keys (`.env`), Implement Retry Logic. |

---

## 🎥 Concept Video Script (6 Minutes)

### The 429 Error (0:00-2:00)
**Visual:** A bouncer stopping you at a club door. "Too many requests."
**Narration:** "Free tiers have limits. Gemini might allow 60 requests/minute. If you send 61, you get HTTP 429: Too Many Requests. A novice script crashes. An Architect's script waits."

### The .env Vault (2:00-4:00)
**Visual:** A hacker scanning GitHub for API keys.
**Narration:** "The fastest way to lose your API access is to commit your key to GitHub. Scrapers find it in seconds. We use **Environment Variables**. Your code says `os.getenv('API_KEY')`. The key lives in a hidden `.env` file on your computer, which is ignored by Git."

### Retry Logic: The "Exponential Backoff" (4:00-6:00)
**Visual:** A graph showing wait times: 1s, 2s, 4s, 8s.
**Narration:** "If the API is busy, don't spam it. Wait 1 second. Still busy? Wait 2. Still busy? Wait 4. This is **Exponential Backoff**. It's the polite (and effective) way to handle traffic jams."

---

## 🧪 Lab 06: Rate Limit Resilience

### Scenario
You are processing a batch of 50 text files. The API limit is simulated to be 5 requests per minute (very strict).

### Step 1: The Crash
**Task:**
1.  Write a loop that prints "Request {i}" 10 times instantly.
2.  Simulate a failure: If `i > 5`, raise an Exception "429: Rate Limit Exceeded".
3.  Observe your script crashing.

### Step 2: The Retry Wrapper
**Task:**
Write a decorator or function wrapper:
```python
import time

def resilient_request(func):
    retries = 3
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if "429" in str(e):
                wait_time = 2 ** i  # 1, 2, 4
                print(f"Hit limit. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise e
```

### Step 3: The Secret Vault
**Task:**
1.  Create a `.env` file: `MY_SECRET=Hunter2`.
2.  Add `.env` to your `.gitignore`.
3.  Write a script to print `os.getenv('MY_SECRET')`.
4.  Verify the key is loaded but NOT visible in your git status.

---

## 🧠 Reflection
**Write 3 sentences:**
1.  Why is Exponential Backoff better than just `time.sleep(1)`?
2.  What is the worst-case scenario if you commit an API key to a public repo?
3.  How do constraints (like free tiers) actually make you a better programmer?
