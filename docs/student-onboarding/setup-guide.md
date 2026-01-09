# Student Setup Guide
**Getting Started with The AI Orchestrator**

---

## 🏁 Phase 0: The Prerequisites
Before you write a line of code, you need the tools of the trade. And remember: **Everything is $0.**

### 1. The Code Editor (IDE)
You need a place to write code.
*   **Recommended:** [VS Code](https://code.visualstudio.com/) (Standard, lightweight)
*   **Alternative:** [Cursor](https://cursor.sh/) (VS Code fork with built-in AI - has a free tier)

### 2. Python Environment
You need Python 3.10 or higher.
*   **Windows:** Download from python.org. Check "Add Python to PATH" during install.
*   **Mac/Linux:** Use `brew install python` or your package manager.
*   **Verify:** Open terminal and type `python --version`.

### 3. The API Keys (Your "Passports")
You need access to the AI models.
1.  **Google Gemini:** Go to [aistudio.google.com](https://aistudio.google.com/). Create a free API key.
2.  **Anthropic Claude:** Sign up at [claude.ai](https://claude.ai) for the chat interface. (API access might have waitlist/cost, but the chat is free).
3.  **HuggingFace:** Create an account at [huggingface.co](https://huggingface.co/) for open-source models.

**⚠️ SECURITY WARNING:** Never share these keys. Never commit them to GitHub.

---

## 🛠️ Phase 1: Repository Setup

### 1. Clone the Repo
```bash
git clone https://github.com/StrayDogSyn/Orchestration.git
cd Orchestration
```

### 2. Virtual Environment
Keep your dependencies clean.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a file named `.env` in the root folder. Add your keys:
```text
GEMINI_API_KEY=your_key_here
```

---

## 🚀 Phase 2: The "Hello World" Test
Run this script to verify your setup:

```python
# test_setup.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Hello! Are you ready to code?")
print(response.text)
```

If it prints a response, you are ready to begin **Module 1**.
