# Lab 01: Fix the AI's Homework - Starter Notebook
**Module 01, Lecture 01: The Architect's Advantage**

---

## Setup

Run this cell first to ensure you're in a clean environment:

```python
# Imports
import time
from typing import List, Dict, Optional

print("✅ Environment ready!")
```

---

## The Scenario

You're building a **job application tracker** for justice-impacted job seekers. 

An "AI enthusiast" on your team used ChatGPT to generate this code. Your job: **review it like an architect.**

---

## The Code (AI-Generated)

```python
class JobTracker:
    """Track job applications - AI-generated version"""
    
    def __init__(self):
        self.applications = []  # List of dicts
    
    def add_application(self, company: str, position: str, date: str) -> None:
        """Add a new job application"""
        self.applications.append({
            'company': company,
            'position': position,
            'date': date,
            'status': 'pending'
        })
    
    def find_by_company(self, company: str) -> List[Dict]:
        """Find all applications to a specific company"""
        results = []
        for app in self.applications:
            if app['company'] == company:
                results.append(app)
        return results
    
    def update_status(self, company: str, position: str, new_status: str) -> bool:
        """Update the status of a specific application"""
        for app in self.applications:
            if app['company'] == company and app['position'] == position:
                app['status'] = new_status
                return True
        return False
    
    def get_all_applications(self) -> List[Dict]:
        """Get all applications"""
        return self.applications
```

---

## Task 1: Complexity Analysis (5 minutes)

**Question**: If you have 1,000 applications, what's the time complexity of `find_by_company("Google")`?

**Your answer** (write below):
```
Time Complexity: O(?)

Reasoning:



```

**Hint**: How many items does Python check in the worst case?

---

## Task 2: Architect's Diagnosis (5 minutes)

**Question**: What data structure would make `find_by_company()` run in O(1) instead of O(n)?

**Your answer**:
```
Better Data Structure: 

Trade-off:


```

---

## Task 3: The Architect's Prompt (10 minutes)

Now you'll prompt an AI to fix this. Write your prompt below.

**❌ Bad Example**: "Make find_by_company() faster"

**✅ Good Example**: See lecture for the full architect's prompt

**YOUR PROMPT** (write it here before running AI):
```
[Your prompt to ChatGPT/Claude goes here]





```

**AI's Response** (paste it here after submitting):
```
[Paste the AI's full response here]





```

---

## Task 4: Test the Original Version (3 minutes)

Let's measure the current performance:

```python
# Initialize tracker with original code
tracker = JobTracker()

# Add 1000 test applications
print("Adding 1000 applications...")
start = time.time()

for i in range(1000):
    company = f"Company_{i % 100}"  # 100 unique companies
    position = f"Position_{i % 50}"  # 50 unique positions
    tracker.add_application(company, position, "2025-01-01")

end = time.time()
print(f"✅ Adding took: {end - start:.4f} seconds\n")

# Test lookup performance
print("Testing find_by_company() performance...")
start = time.time()
results = tracker.find_by_company("Company_42")
end = time.time()

print(f"✅ Found {len(results)} applications")
print(f"✅ Lookup took: {(end - start) * 1000:.4f} milliseconds")
```

**Record Your Results**:
```
Add Time: _____ seconds
Lookup Time: _____ milliseconds
Number Found: _____ applications
```

---

## Task 5: Implement the AI's Solution (5 minutes)

Paste the AI's refactored code here and test it:

```python
# PASTE THE AI'S REFACTORED CODE HERE

class JobTrackerOptimized:
    """Your AI-generated optimized version"""
    
    def __init__(self):
        # TODO: Replace with AI's suggested structure
        pass
    
    # TODO: Paste AI's methods here






```

---

## Task 6: Test the Optimized Version (3 minutes)

```python
# Test the optimized version
tracker_v2 = JobTrackerOptimized()

# Add same 1000 applications
print("Adding 1000 applications to optimized version...")
start = time.time()

for i in range(1000):
    company = f"Company_{i % 100}"
    position = f"Position_{i % 50}"
    tracker_v2.add_application(company, position, "2025-01-01")

end = time.time()
print(f"✅ Adding took: {end - start:.4f} seconds\n")

# Test lookup performance
print("Testing optimized find_by_company()...")
start = time.time()
results = tracker_v2.find_by_company("Company_42")
end = time.time()

print(f"✅ Found {len(results)} applications")
print(f"✅ Lookup took: {(end - start) * 1000:.4f} milliseconds")
```

**Record Your Results**:
```
Add Time: _____ seconds
Lookup Time: _____ milliseconds
Speedup: _____ x faster
```

---

## Task 7: Verification Questions (2 minutes)

Answer these before submitting:

**1. Did the AI explain WHY the change improves performance?**
```
YES / NO

If yes, summarize the explanation:



```

**2. Did the AI mention any trade-offs (e.g., memory usage)?**
```
YES / NO

If yes, what trade-off:


```

**3. What happens if you need multiple applications to the same company?**
```
Does the optimized version handle this?

YES / NO / UNCLEAR

Explain:


```

---

## Reflection (5 minutes)

Answer in 2-3 sentences each:

**Reflection 1: The Architect Test**
> If you had to explain to a non-technical friend why YOU matter more than the AI in this process, what would you say?

```
Your answer:




```

**Reflection 2: The Verification Test**
> The AI's code works perfectly now. But what happens if tomorrow you need to track "multiple applications to the same company for the same position on different dates"? Who catches that the data structure needs to change—you or the AI?

```
Your answer:




```

**Reflection 3: The Growth Test**
> One year from now, what will be MORE valuable: knowing 10 more frameworks, or understanding data structures deeply?

```
Your answer:




```

---

## Submission

Export this notebook and submit:

1. Your completed answers above
2. Your "Architect's Prompt" (Task 3)
3. The AI's full response
4. Both test results (original vs optimized)
5. Your three reflections

---

## Beta Tester Notes (For Hunter)

**Time Log**:
- Start Time: _______
- End Time: _______
- Total Duration: _______

**Friction Points** (where you got stuck):
1. 
2. 
3. 

**Aha Moments** (where things clicked):
1. 
2. 
3. 

**Would you recommend this to past-you?**: YES / NO / MAYBE

**Why?**:
```



```

---

**Last Updated**: December 23, 2025  
**Version**: 0.1.0 (Beta Test)
