# 🚀 Quick Start Guide

> Get from zero to learning in 3 steps.

---

## You Are Here

You've just discovered The AI Orchestrator bootcamp. This guide gets you from setup to learning in 15 minutes.

---

## Step 1: Clone the Repository (2 minutes)

```bash
# Clone the repository
git clone https://github.com/StrayDogSyn/Orchestration.git
cd Orchestration

# Create your environment file
cp .env.example .env
```

---

## Step 2: Get Your API Keys (10 minutes)

All services have **free tiers**. You'll need at least one to start.

### Google Gemini (Recommended First)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key to your `.env` file:
   ```
   GEMINI_API_KEY=your_key_here
   ```

### OpenAI (Optional - $5 Free Credit)

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account
3. Navigate to API Keys → **"Create new secret key"**
4. Copy to `.env`:
   ```
   OPENAI_API_KEY=your_key_here
   ```

### Anthropic Claude (Optional)

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create an account and verify email
3. Navigate to API Keys → **"Create Key"**
4. Copy to `.env`:
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```

---

## Step 3: Install Dependencies (3 minutes)

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ✅ You're Ready!

### Start Learning

1. **Begin with Module 1**: [modules/01-foundations/](modules/01-foundations/)
2. **Read the module README** for objectives and structure
3. **Complete lectures** → **labs** → **projects**

### Verify Your Setup

Run this quick test to verify your API keys work:

```python
# test_setup.py
import os
from dotenv import load_dotenv

load_dotenv()

# Check which API keys are configured
apis = {
    "Gemini": os.getenv("GEMINI_API_KEY"),
    "OpenAI": os.getenv("OPENAI_API_KEY"),
    "Anthropic": os.getenv("ANTHROPIC_API_KEY"),
}

print("🔑 API Key Status:")
for name, key in apis.items():
    status = "✅ Configured" if key and key != f"your_{name.lower()}_api_key_here" else "❌ Not set"
    print(f"   {name}: {status}")

configured = sum(1 for k in apis.values() if k and "your_" not in k)
print(f"\n{'🎉 Ready to go!' if configured > 0 else '⚠️  Please configure at least one API key'}")
```

```bash
python test_setup.py
```

---

## 📚 What's Next?

### Course Structure

```
Module 1: Foundations     → Weeks 1-3   → Why fundamentals matter
Module 2: Prompt Eng.     → Weeks 4-6   → Prompts as code
Module 3: Orchestration   → Weeks 7-9   → Multi-model workflows
Module 4: Memory & RAG    → Weeks 10-12 → Persistent AI systems
Module 5: Agents          → Weeks 13-15 → Multi-agent architectures
Module 6: Capstone        → Weeks 16-24 → Build your AI platform
```

### Self-Paced Tips

- ⏰ **Pace yourself**: 5-10 hours/week is ideal
- 📝 **Complete every lab**: Hands-on practice is essential
- 🔄 **Review before moving on**: Each module builds on the last
- ❓ **Ask for help**: Open a GitHub Discussion if stuck

---

## 🆘 Getting Help

- **Documentation**: Browse the [docs/](docs/) directory
- **Issues**: Found a bug? [Open an issue](https://github.com/StrayDogSyn/Orchestration/issues)
- **Discussions**: Questions? [Start a discussion](https://github.com/StrayDogSyn/Orchestration/discussions)

---

## 💡 Prerequisites Reminder

Before starting Module 1, you should be comfortable with:

- ✅ Object-Oriented Programming (classes, inheritance)
- ✅ Data Structures (arrays, trees, hash maps)
- ✅ Algorithms (sorting, searching, Big O)
- ✅ Python basics (functions, loops, error handling)

Not there yet? No problem! Build these skills first, then return. We'll be here.

---

<div align="center">

**Ready to become an AI-augmented developer?**

[Start Module 1 →](modules/01-foundations/)

</div>
