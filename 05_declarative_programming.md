# Programming Paradigms Series - Article 5: Declarative Programming

**Series Navigation:** [← Functional Programming](04_functional_programming.md) | Article 5 of 7 | Next: [Procedural Programming →](06_procedural_programming.md)

---

**About This Series**

This article series represents my journey of learning and applying fundamental programming concepts to the Dart programming language. These are my detailed notes and insights from the learning process, which I hope will be valuable to others exploring similar topics.

---

## Table of Contents

1. [Concept](#concept)
2. [Real-Life Analogy](#real-life-analogy)
3. [Dart Example](#dart-example)
4. [Declarative vs Imperative Comparison](#declarative-vs-imperative-comparison)
5. [Real-World Examples](#real-world-examples)

---

## Concept

Declarative programming focuses on *what* you want to achieve rather than *how* to achieve it. You describe the desired result, and the system figures out the steps.

## Real-Life Analogy

When you order food at a restaurant, you use declarative style:
- **Declarative**: "I want a medium pepperoni pizza"
- **Imperative**: "Take dough, spread sauce, add cheese, add pepperoni, bake at 450°F for 12 minutes"

You declare what you want; the chef handles the how.

## Dart Example

```dart
void main() {
  List<Map<String, dynamic>> users = [
    {'name': 'Alice', 'age': 25, 'country': 'USA'},
    {'name': 'Bob', 'age': 30, 'country': 'UK'},
    {'name': 'Charlie', 'age': 22, 'country': 'USA'},
    {'name': 'Diana', 'age': 28, 'country': 'Canada'},
  ];

  // Declarative approach: describe what you want
  var usersOver25InUSA = users
      .where((user) => user['age'] > 25)
      .where((user) => user['country'] == 'USA')
      .toList();

  print('Users over 25 in USA: $usersOver25InUSA');

  // Compare with imperative approach
  List<Map<String, dynamic>> result = [];
  for (var user in users) {
    if (user['age'] > 25 && user['country'] == 'USA') {
      result.add(user);
    }
  }
  print('Imperative result: $result');
}

// Declarative widget building in Flutter (Dart's UI framework)
class UserProfile extends StatelessWidget {
  final String name;
  final int age;

  UserProfile({required this.name, required this.age});

  @override
  Widget build(BuildContext context) {
    // We declare what the UI should look like
    return Column(
      children: [
        Text('Name: $name'),
        Text('Age: $age'),
        ElevatedButton(
          onPressed: () {},
          child: Text('View Profile'),
        ),
      ],
    );
  }
}
```

## Declarative vs Imperative Comparison

```
╔═══════════════════════════════════════════════════════════════╗
║           💡 IMPERATIVE (How to do it) 💡                    ║
╠═══════════════════════════════════════════════════════════════╣
║  "Tell me HOW to make coffee step by step" ☕                ║
║                                                               ║
║  1. 🥤 Get a cup                                              ║
║  2. ☕ Put coffee grounds in filter                           ║
║  3. 💧 Add water to machine                                   ║
║  4. 🔌 Turn on machine                                        ║
║  5. ⏰ Wait for brewing                                       ║
║  6. 🫗 Pour into cup                                          ║
║                                                               ║
║  🎯 Focus: Explicit control flow and state changes            ║
║  📝 You specify: Every single step                            ║
║  ⚙️ Control: High (you manage everything)                     ║
╚═══════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════╗
║          📋 DECLARATIVE (What you want) 📋                   ║
╠═══════════════════════════════════════════════════════════════╣
║  "I want a cup of coffee" ☕                                  ║
║                                                               ║
║  Result: You get coffee ☕✨                                   ║
║  (Implementation details are abstracted away)                 ║
║                                                               ║
║  🎯 Focus: Desired outcome, not the process                   ║
║  📝 You specify: What you want (the result)                   ║
║  ⚙️ Control: Low (system handles the "how")                   ║
╚═══════════════════════════════════════════════════════════════╝
```

### Code Comparison

```
╔═══════════════════════════════════════════════════════════════╗
║                    💡 IMPERATIVE CODE 💡                     ║
╚═══════════════════════════════════════════════════════════════╝

┌───────────────────────────────────────────┐
│ List result = [];                         │  📝 Create empty list
│ for (user in users) {                     │  🔄 Manual iteration
│   if (user.age > 25 &&                    │  ❓ Explicit conditions
│       user.country == 'USA') {            │
│     result.add(user);                     │  ➕ Manual addition
│   }                                       │
│ }                                         │
│                                           │
│ ⚙️ Manual iteration, explicit conditions   │
│ 📊 ~7 lines of code                       │
│ 🎯 You control: Loop, conditions, updates │
└───────────────────────────────────────────┘
              │
              ▼
     🔧 Steps clearly defined
     🎮 Full control over process

╔═══════════════════════════════════════════════════════════════╗
║                   📋 DECLARATIVE CODE 📋                     ║
╚═══════════════════════════════════════════════════════════════╝

┌───────────────────────────────────────────┐
│ users                                     │  📦 Start with data
│   .where(age > 25)                        │  🔍 Filter by age
│   .where(country == 'USA')                │  🔍 Filter by country
│                                           │
│ 🎨 Describe the criteria, not the process │
│ 📊 ~2 lines of code                       │
│ 🎯 System handles: How to iterate/filter  │
└───────────────────────────────────────────┘
              │
              ▼
     ✨ What we want, not how
     🎪 System handles implementation
```

## Real-World Examples

```
╔═══════════════════════════════════════════════════════════════╗
║         🌍 DECLARATIVE EXAMPLES IN DAILY LIFE 🌍             ║
╚═══════════════════════════════════════════════════════════════╝

📝 HTML:
┌─────────────────────────────────────┐
│ <button>Click Me</button>           │
│                                     │
│ ↑ What you want (a button)          │
│   Not how to draw it                │
└─────────────────────────────────────┘

🗄️ SQL:
┌─────────────────────────────────────┐
│ SELECT * FROM users WHERE age > 25  │
│                                     │
│ ↑ What data you want                │
│   Not how to retrieve it            │
└─────────────────────────────────────┘

🎨 CSS:
┌─────────────────────────────────────┐
│ .button { color: blue; }            │
│                                     │
│ ↑ What style you want               │
│   Not how to apply it               │
└─────────────────────────────────────┘

📱 React/Flutter:
┌─────────────────────────────────────┐
│ Widget build() {                    │
│   return Text('Hello');             │
│ }                                   │
│                                     │
│ ↑ What UI you want                  │
│   Not how to render it              │
└─────────────────────────────────────┘

🍕 Restaurant Analogy:
┌─────────────────────────────────────┐
│ DECLARATIVE:                        │
│ "I want a pepperoni pizza" 🍕       │
│                                     │
│ IMPERATIVE:                         │
│ "Take dough, roll it flat, spread   │
│  sauce, add cheese, add pepperoni,  │
│  bake at 450°F for 12 minutes" 🍕  │
└─────────────────────────────────────┘
```

Declarative programming is particularly powerful for UI development, database queries, and configuration. By focusing on what you want rather than how to get it, declarative code tends to be more concise, readable, and easier to maintain. Flutter's widget system is an excellent example of declarative UI programming in Dart.

---

**Series Navigation:** [← Functional Programming](04_functional_programming.md) | Article 5 of 7 | Next: [Procedural Programming →](06_procedural_programming.md)

**Other Articles in This Series:**
- [Article 1: What Are Programming Paradigms?](01_what_are_programming_paradigms.md)
- [Article 2: Imperative Programming](02_imperative_programming.md)
- [Article 3: Object-Oriented Programming (OOP)](03_oop.md)
- [Article 4: Functional Programming](04_functional_programming.md)
- **Article 5: Declarative Programming** (Current)
- [Article 6: Procedural Programming](06_procedural_programming.md)
- [Article 7: Choosing the Right Paradigm - Summary and Best Practices](07_summary.md)
