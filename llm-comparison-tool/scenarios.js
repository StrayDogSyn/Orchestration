export const scenarios = [
  {
    id: "code-explanation",
    title: "Test 1: Code Explanation (Array Fundamentals)",
    description:
      "Test the model's ability to explain core CS concepts including hidden pitfalls.",
    prompt:
      "Explain how array insertion works in Python logic vs C logic. What happens in memory when I insert an element at index 0 of an array of size 1 million?",
    rubric: [
      { text: "Explains O(n) time complexity for insertion", weight: 20 },
      { text: "Mentions shifting of elements (memory movement)", weight: 20 },
      {
        text: "Distinguishes between Python Lists (dynamic arrays) and C arrays",
        weight: 20,
      },
      {
        text: "Mentions potential performance impact/freezing for large N",
        weight: 20,
      },
      {
        text: "Suggests better data structures (deque/linked list) for this use case",
        weight: 20,
      },
    ],
  },
  {
    id: "debugging",
    title: "Test 2: Debugging Assistance (Off-by-One)",
    description:
      "Evaluate if the model finds the root cause and teaches the debugging process.",
    prompt:
      "My loop isn't printing the last element of my list. Help? \n```python\nmy_list = ['a', 'b', 'c']\nfor i in range(len(my_list) - 1):\n    print(my_list[i])\n```",
    rubric: [
      { text: "Identifies the off-by-one error in range()", weight: 25 },
      {
        text: "Explains clearly that range() is exclusive at the end",
        weight: 25,
      },
      { text: "Provides the corrected code snippet", weight: 25 },
      {
        text: "Suggests a Pythonic alternative (iterating directly over list)",
        weight: 25,
      },
    ],
  },
  {
    id: "refactoring",
    title: "Test 3: Refactoring (Big O optimization)",
    description:
      "Check if the model identifies inefficient nested loops and optimizes them.",
    prompt:
      "Review this code for performance. It checks if items from list A exist in list B.\n```python\nmatches = []\nfor a in list_a: # size 10k\n    for b in list_b: # size 10k\n        if a == b:\n            matches.append(a)\n```",
    rubric: [
      { text: "Identifies O(n*m) or quadratic complexity", weight: 30 },
      {
        text: "Suggests converting list_b to a set for O(1) lookups",
        weight: 30,
      },
      {
        text: "Provides the optimized solution with O(n) complexity",
        weight: 20,
      },
      { text: "Explains WHY sets are faster (hashing)", weight: 20 },
    ],
  },
  {
    id: "socratic-1",
    title: "Test 4: Socratic Pedagogy #1 (Recursion)",
    description: "Does the model guide the student or just give the answer?",
    prompt:
      "I don't understand recursion. Can you write a recursive factorial function for me?",
    rubric: [
      { text: "DOES NOT immediately give the full code solution", weight: 30 },
      {
        text: "Explains the concept of 'base case' and 'recursive step'",
        weight: 30,
      },
      {
        text: "Asks a guiding question to check understanding first",
        weight: 20,
      },
      {
        text: "Uses a simple analogy (e.g., Russian dolls, standing in line)",
        weight: 20,
      },
    ],
  },
  {
    id: "socratic-2",
    title: "Test 5: Socratic Pedagogy #2 (Security)",
    description: "Does the model catch security risks immediately?",
    prompt:
      "I'm pushing my code to GitHub but it's not working. Here is my setup: \n```python\napi_key = 'sk-12345-actual-secret-key'\ncall_api(api_key)\n```",
    rubric: [
      {
        text: "IMMEDIATELY warns about exposed API key (Critical)",
        weight: 40,
      },
      { text: "Advises to revoke/rotate the key immediately", weight: 30 },
      {
        text: "Explains how to use .env files or environment variables",
        weight: 30,
      },
    ],
  },
];
