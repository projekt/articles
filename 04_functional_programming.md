# Programming Paradigms Series - Article 4: Functional Programming

**⏱️ 7-Minute Read**

**Series Navigation:** [← Object-Oriented Programming](03_oop.md) | Article 4 of 7 | Next: [Declarative Programming →](05_declarative_programming.md)

---

**About This Series**

This article series represents my journey of learning and applying fundamental programming concepts to the Dart programming language. These are my detailed notes and insights from the learning process, which I hope will be valuable to others exploring similar topics.

---

## Table of Contents

1. [Concept](#concept)
2. [Real-Life Analogy](#real-life-analogy)
3. [Dart Example](#dart-example)
4. [Functional Programming Pipeline](#functional-programming-pipeline)
5. [Pure vs Impure Functions](#pure-vs-impure-functions)
6. [Immutability Concept](#immutability-concept)
7. [Higher-Order Functions](#higher-order-functions)

---

## Concept

Functional programming treats computation as the evaluation of mathematical functions. It emphasizes immutability (data that doesn't change) and avoids side effects (changes to state outside the function).

## Real-Life Analogy

Think of a vending machine for drinks. You put in money and a selection code, and you get a drink out. The machine doesn't remember your previous purchases or change its behavior based on past interactions. Each transaction is independent:
- **Input**: money + selection
- **Output**: drink
- **No side effects**: The machine's core function doesn't change based on history

## Dart Example

```dart
void main() {
  // Functional approach to calculate sum of squares
  List<int> numbers = [1, 2, 3, 4, 5];

  // Using functional methods: map and reduce
  int sum = numbers
      .map((n) => n * n)           // Transform each number to its square
      .reduce((a, b) => a + b);    // Combine all squares into sum

  print('Sum of squares: $sum');   // Output: 55

  // Pure function example
  int multiply(int a, int b) {
    return a * b;  // Always returns same output for same input
  }

  // Higher-order function (function that takes functions as parameters)
  List<int> applyOperation(List<int> numbers, int Function(int) operation) {
    return numbers.map(operation).toList();
  }

  List<int> doubled = applyOperation(numbers, (n) => n * 2);
  print('Doubled: $doubled');  // [2, 4, 6, 8, 10]

  // Immutability example
  final originalList = [1, 2, 3];
  final newList = [...originalList, 4];  // Create new list instead of modifying

  print('Original: $originalList');  // [1, 2, 3] - unchanged
  print('New: $newList');            // [1, 2, 3, 4]
}

// Pure function - no side effects
int calculateDiscount(int price, double discountRate) {
  return (price * (1 - discountRate)).round();
}

// Impure function - has side effects (modifies external state)
int counter = 0;
void incrementCounter() {
  counter++;  // Side effect: modifies external variable
}
```

## Functional Programming Pipeline

```
╔═══════════════════════════════════════════════════════════╗
║         🧮 FUNCTIONAL TRANSFORMATION PIPELINE 🧮         ║
╚═══════════════════════════════════════════════════════════╝

Input Data: [1, 2, 3, 4, 5] 📥
     │
     │ map(n => n²)
     ▼
┌─────────────────────┐
│  🔄 TRANSFORM       │
│  ───────────────    │
│  [1, 4, 9, 16, 25]  │  ← Each element squared
└──────────┬──────────┘
           │
           │ reduce((a, b) => a + b)
           ▼
┌─────────────────────┐
│  ➕ AGGREGATE       │
│  ───────────────    │
│  1 + 4 = 5          │
│  5 + 9 = 14         │
│  14 + 16 = 30       │
│  30 + 25 = 55       │
└──────────┬──────────┘
           │
           ▼
    Result: 55 ✨ 📤

🎯 Pure functions → Predictable results → No side effects
```

## Pure vs Impure Functions

```
╔═══════════════════════════════════════════════════════════════╗
║                  ✅ PURE FUNCTION ✅                         ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  int add(int a, int b) {                                      ║
║    return a + b;     // Same input → Same output ✓           ║
║  }                   // No side effects ✓                    ║
║                                                               ║
║  📊 Properties:                                               ║
║  ✓ Deterministic (100% predictable)                          ║
║  ✓ No side effects (doesn't change external state)           ║
║  ✓ Easy to test (input → output, that's it!)                ║
║  ✓ Can be cached (memoization works perfectly)               ║
║  ✓ Thread-safe (parallel execution friendly)                 ║
║                                                               ║
║  Example: add(2, 3) ALWAYS returns 5                          ║
╚═══════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════╗
║                  ❌ IMPURE FUNCTION ❌                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  int counter = 0;                                             ║
║  void increment() {                                           ║
║    counter++;        // Modifies external state ✗            ║
║    print(counter);   // Has side effect (I/O) ✗             ║
║  }                                                            ║
║                                                               ║
║  ⚠️ Issues:                                                   ║
║  ✗ Unpredictable results (depends on external state)         ║
║  ✗ Hard to test (need to set up external state)             ║
║  ✗ Can cause bugs in concurrent code (race conditions)       ║
║  ✗ Difficult to reason about (hidden dependencies)           ║
║  ✗ Cannot be safely cached                                   ║
║                                                               ║
║  Example: increment() returns different values each time      ║
╚═══════════════════════════════════════════════════════════════╝
```

## Immutability Concept

```
╔═══════════════════════════════════════════════════════════════╗
║           🔄 MUTABLE vs 🔒 IMMUTABLE 🔒                      ║
╚═══════════════════════════════════════════════════════════════╝

🔴 Mutable Approach (Imperative):
┌──────────────────┐
│ List: [1, 2, 3]  │ ← Original object
│ Memory: 0x1000   │
└────────┬─────────┘
         │ .add(4)  ← Modifies in place
         ▼
┌──────────────────┐
│ List: [1,2,3,4]  │ ← Same object, changed! ⚠️
│ Memory: 0x1000   │ ← Same memory address
└──────────────────┘

⚠️ Problem: Other references are affected!
   If someone else had a reference to this list,
   they'll see the change unexpectedly.

🟢 Immutable Approach (Functional):
┌──────────────────┐
│ List: [1, 2, 3]  │ ─────────► Still [1, 2, 3] ✓
│ Memory: 0x1000   │            Original unchanged!
└────────┬─────────┘
         │ [...list, 4]  ← Creates new
         ▼
┌──────────────────┐
│ New: [1,2,3,4]   │ ← New object created ✓
│ Memory: 0x2000   │ ← Different memory address
└──────────────────┘

✅ Benefit: Predictable, safe, no surprises!
   Original data is preserved, easier to reason about.
```

## Higher-Order Functions

```
╔═══════════════════════════════════════════════════════════════╗
║            🎯 HIGHER-ORDER FUNCTIONS 🎯                      ║
╚═══════════════════════════════════════════════════════════════╝

A Higher-Order Function is a function that:
  1️⃣ Takes functions as parameters, OR
  2️⃣ Returns a function as a result

┌─────────────────────────────────────────────────────────┐
│         Higher-Order Function Example                   │
│                                                          │
│  applyOperation(numbers, operation)                      │
│         │              │                                 │
│    📦 Data         🔧 Function                           │
│    to process      to apply                              │
└─────────┬───────────────┬──────────────────────────────┘
          │               │
          ▼               ▼
    [1,2,3,4,5]      (n) => n * 2
          │               │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │  🔄 Apply to  │
          │  all elements │
          └───────┬───────┘
                  │
                  ▼
         [2, 4, 6, 8, 10] ✨

Benefits:
✓ Code reusability (same function, different operations)
✓ Abstraction (separate "what to do" from "how to do it")
✓ Composability (combine functions to build complex logic)

Example operations you can pass:
• (n) => n * 2        (double)
• (n) => n * n        (square)
• (n) => n + 10       (add 10)
```

Functional programming shines in data processing and transformation tasks. Its emphasis on pure functions and immutability makes code more predictable, testable, and suitable for parallel execution.

---

## Further Reading

**Functional Programming:**
- [Functional Programming in Dart](https://dart.dev/guides/language/effective-dart/usage#prefer-using-higher-order-methods) - Official guidelines
- [Functional Programming Principles](https://www.freecodecamp.org/news/functional-programming-principles-in-javascript-1b8fc6c3563f/) - Core concepts
- [Why Functional Programming Matters](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf) - Classic paper

**Dart Functional Features:**
- [Iterable Collections](https://dart.dev/codelabs/iterables) - map, where, reduce
- [Functions in Dart](https://dart.dev/guides/language/language-tour#functions) - First-class functions

**Advanced Topics:**
- [Immutability in Practice](https://www.sitepoint.com/immutability-javascript/) - Benefits and techniques
- [Function Composition](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-function-composition-20dfb109a1a0) - Building complex functions

**Books:**
- [Functional Programming in JavaScript](https://www.manning.com/books/functional-programming-in-javascript) - Practical approach
- [Professor Frisby's Mostly Adequate Guide to FP](https://mostly-adequate.gitbook.io/mostly-adequate-guide/) - Free online book

---

## 👤 About the Author

**Srđan Ljustina** - Software Developer & Technical Writer

🌐 [Website](https://srdapp.rs) | 💼 [LinkedIn](https://www.linkedin.com/in/srdjanljustina/) | 💻 [GitHub](https://github.com/projekt)

---

**Series Navigation:** [← Object-Oriented Programming](03_oop.md) | Article 4 of 7 | Next: [Declarative Programming →](05_declarative_programming.md)

**Other Articles in This Series:**
- [Article 1: What Are Programming Paradigms?](01_what_are_programming_paradigms.md)
- [Article 2: Imperative Programming](02_imperative_programming.md)
- [Article 3: Object-Oriented Programming (OOP)](03_oop.md)
- **Article 4: Functional Programming** (Current)
- [Article 5: Declarative Programming](05_declarative_programming.md)
- [Article 6: Procedural Programming](06_procedural_programming.md)
- [Article 7: Choosing the Right Paradigm - Summary and Best Practices](07_summary.md)
