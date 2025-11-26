---
title: "Mastering Git & GitHub | Complete Version Control Guide"
description: "Comprehensive guide to Git and GitHub: version control fundamentals, workflows, branching strategies, collaboration, and best practices for developers."
keywords: "Git, GitHub, version control, git commands, branching, merging, pull requests, collaboration, repository management"
author: "Srđan Ljuština"
date: "2024-11-26"
reading_time: "25 minutes"
canonical_url: "https://projekt.github.io/articles/git_github_complete_guide.html"
---

# Mastering Git & GitHub: A Complete Guide to Modern Version Control

**⏱️ 25-Minute Deep Dive**

A Comprehensive Guide with Visual Diagrams, Real-World Examples, and Best Practices

---

**About This Article**

This article represents my journey of learning and mastering Git and GitHub, the fundamental tools for modern software development. These are my detailed notes and insights from the learning process, which I hope will be valuable to others exploring version control and collaborative development.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
   - [Overview](#overview)
   - [Key Takeaways](#key-takeaways)
   - [What You'll Learn](#what-youll-learn)
   - [Who Should Read This](#who-should-read-this)
2. [Introduction](#introduction)
3. [Understanding Version Control](#understanding-version-control)
   - [Why Version Control Matters](#why-version-control-matters)
   - [Real-World Analogy](#real-world-analogy)
4. [Git Fundamentals](#git-fundamentals)
   - [What is Git?](#what-is-git)
   - [Core Git Concepts](#core-git-concepts)
   - [The Three States](#the-three-states)
5. [Essential Git Commands](#essential-git-commands)
   - [Repository Initialization](#repository-initialization)
   - [Basic Workflow Commands](#basic-workflow-commands)
   - [Branching and Merging](#branching-and-merging)
   - [Remote Operations](#remote-operations)
6. [GitHub: Git in the Cloud](#github-git-in-the-cloud)
   - [What is GitHub?](#what-is-github)
   - [GitHub vs Git](#github-vs-git)
   - [Key GitHub Features](#key-github-features)
7. [Branching Strategies](#branching-strategies)
   - [Feature Branch Workflow](#feature-branch-workflow)
   - [Git Flow](#git-flow)
   - [GitHub Flow](#github-flow)
8. [Collaboration Workflows](#collaboration-workflows)
   - [Pull Requests](#pull-requests)
   - [Code Reviews](#code-reviews)
   - [Resolving Merge Conflicts](#resolving-merge-conflicts)
9. [Visual Representations](#visual-representations)
   - [Diagram 1: Git Workflow](#diagram-1-git-workflow)
   - [Diagram 2: Branching Model](#diagram-2-branching-model)
   - [Diagram 3: Pull Request Flow](#diagram-3-pull-request-flow)
10. [Best Practices](#best-practices)
    - [Commit Messages](#commit-messages)
    - [Branch Naming](#branch-naming)
    - [Repository Organization](#repository-organization)
11. [Common Scenarios and Solutions](#common-scenarios-and-solutions)
    - [Undoing Changes](#undoing-changes)
    - [Stashing Work](#stashing-work)
    - [Cherry-Picking Commits](#cherry-picking-commits)
12. [Advanced Topics](#advanced-topics)
    - [Rebasing](#rebasing)
    - [Git Hooks](#git-hooks)
    - [Submodules](#submodules)
13. [Conclusion](#conclusion)
14. [Further Reading](#further-reading)

---

## Executive Summary

### Overview

This comprehensive guide explores Git and GitHub, the essential tools for modern software development. Git provides powerful version control capabilities that track every change to your codebase, while GitHub extends Git with collaboration features, making team development seamless and efficient.

### Key Takeaways

- **Version Control Fundamentals:** Git tracks every change, enabling you to revert mistakes, compare versions, and maintain a complete project history

- **Distributed Architecture:** Every developer has a complete copy of the repository, enabling offline work and reducing single points of failure

- **Branching Power:** Git's lightweight branching enables parallel development, experimentation, and organized feature development

- **Collaboration Made Easy:** GitHub's pull requests, code reviews, and issue tracking facilitate team collaboration and code quality

- **Industry Standard:** Git and GitHub are used by millions of developers and virtually all modern software projects

- **Best Practices Matter:** Following conventions for commits, branches, and workflows leads to maintainable, professional codebases

### What You'll Learn

- **Git Fundamentals:** Core concepts, commands, and workflows
- **Repository Management:** Initializing, cloning, and maintaining repositories
- **Branching Strategies:** Feature branches, Git Flow, and GitHub Flow
- **Collaboration:** Pull requests, code reviews, and team workflows
- **Problem Solving:** Handling conflicts, undoing changes, and advanced scenarios
- **Best Practices:** Professional conventions and patterns

### Who Should Read This

- **Beginners:** New to version control or Git
- **Students:** Learning software development fundamentals
- **Professional Developers:** Wanting to deepen Git knowledge
- **Team Leads:** Establishing workflows and best practices
- **Anyone:** Working on software projects, whether solo or in teams

---

## Introduction

Imagine working on a document and accidentally deleting an important paragraph. Or imagine collaborating with teammates on the same file and losing track of who changed what. Now imagine having a time machine that records every change, lets you travel back to any previous version, and seamlessly merges everyone's work together. That's exactly what Git and GitHub provide for software development.

Git has revolutionized how developers work, transforming from chaotic file copying and naming conventions (like `final_version_v2_REALLY_FINAL.txt`) to an organized, powerful system that tracks every change, enables fearless experimentation, and facilitates seamless collaboration.

---

## Understanding Version Control

### Why Version Control Matters

Version control solves fundamental problems in software development:

**Problem 1: Change Tracking**
- ❌ Without version control: Which line changed? When? Why?
- ✅ With version control: Complete history of every change with reasons

**Problem 2: Collaboration**
- ❌ Without version control: Overwriting each other's changes, email attachments, confusion
- ✅ With version control: Parallel work with automatic merging

**Problem 3: Backup and Recovery**
- ❌ Without version control: Lost work, manual backups, no rollback
- ✅ With version control: Every version saved, easy rollback to any point

**Problem 4: Experimentation**
- ❌ Without version control: Fear of breaking working code
- ✅ With version control: Create branches, experiment freely, discard or merge

### Real-World Analogy

Think of Git like a sophisticated **"save game" system in video games**, but for code:

- **Saves (Commits):** Just like saving your progress in a game, commits save your code's state
- **Multiple Save Slots (Branches):** Try different strategies without losing your main progress
- **Load Previous Save (Checkout):** Travel back to any previous state
- **Merge Strategies:** Combine successful experiments into your main game
- **Multiplayer (GitHub):** Share your save files and collaborate with other players

---

## Git Fundamentals

### What is Git?

Git is a **distributed version control system (DVCS)** created by Linus Torvalds in 2005. Unlike older centralized systems, Git gives every developer a complete copy of the repository, including its full history.

```
╔═══════════════════════════════════════════════════════════╗
║              🎯 CENTRALIZED VS DISTRIBUTED 🎯            ║
╚═══════════════════════════════════════════════════════════╝

CENTRALIZED (Old Way)                DISTRIBUTED (Git)

     [Central Server]                 [GitHub/Remote]
           │                               │
           │                        ┌──────┼──────┐
     ┌─────┼─────┐                  │      │      │
     │     │     │                  │      │      │
  [Dev A][Dev B][Dev C]         [Dev A][Dev B][Dev C]
                                 (Full)  (Full)  (Full)
  ❌ Single point of failure      ✅ Every copy is complete
  ❌ Need network to work          ✅ Work offline
  ❌ Slow operations               ✅ Fast local operations
```

### Core Git Concepts

**1. Repository (Repo)**
A repository is a directory containing your project files and the complete history of all changes.

```bash
# A repository contains:
project/
├── .git/              # Git's internal database (DON'T TOUCH!)
├── src/               # Your actual files
├── README.md
└── .gitignore
```

**2. Commit**
A commit is a snapshot of your project at a specific point in time. Think of it as a save point.

```
Each commit contains:
- Snapshot of all files
- Author information
- Timestamp
- Commit message (description)
- Parent commit reference
- Unique SHA-1 hash (ID)
```

**3. Branch**
A branch is an independent line of development. The default branch is usually called `main` or `master`.

```
        main branch
    A --- B --- C --- D
               \
                E --- F (feature branch)
```

**4. Remote**
A remote is a version of your repository hosted elsewhere (like on GitHub).

### The Three States

Git has three main states that your files can be in:

```
╔══════════════════════════════════════════════════════════╗
║              🎯 THE THREE STATES OF GIT 🎯              ║
╚══════════════════════════════════════════════════════════╝

1️⃣ WORKING DIRECTORY          2️⃣ STAGING AREA           3️⃣ REPOSITORY
   (Modified)                    (Staged)                  (Committed)

   📝 file.txt                   📋 Staged                 💾 Saved
   You're editing                Ready to commit           Permanent record

   [Edit files]  ──git add──>  [Stage changes] ──git commit──> [Save to history]

                 <──git restore──              <──git checkout──
                    [Discard]                    [Time travel]
```

**1. Working Directory:** Your actual files where you make changes

**2. Staging Area (Index):** A preview of your next commit; you choose what to include

**3. Repository (Committed):** Permanent record in Git's database

---

## Essential Git Commands

### Repository Initialization

**Creating a New Repository:**
```bash
# Start a new Git repository
git init

# This creates a .git directory containing all Git metadata
```

**Cloning an Existing Repository:**
```bash
# Clone from GitHub or other remote
git clone https://github.com/username/repository.git

# Clone with a custom directory name
git clone https://github.com/username/repository.git my-project
```

**Checking Repository Status:**
```bash
# See which files are modified, staged, or untracked
git status

# Shorter status output
git status -s
```

### Basic Workflow Commands

**The Basic Git Workflow:**

```
╔════════════════════════════════════════════════════════╗
║           🔄 BASIC GIT WORKFLOW 🔄                    ║
╚════════════════════════════════════════════════════════╝

1. Make changes to files
   📝 Edit, create, delete files

2. Stage changes
   $ git add filename.txt        # Stage specific file
   $ git add .                   # Stage all changes

3. Commit staged changes
   $ git commit -m "Add new feature"

4. Push to remote (GitHub)
   $ git push origin main
```

**Adding Files to Staging:**
```bash
# Stage a specific file
git add file.txt

# Stage all files in directory
git add .

# Stage all modified files (not new untracked files)
git add -u

# Interactive staging
git add -p
```

**Committing Changes:**
```bash
# Commit with inline message
git commit -m "Fix bug in user authentication"

# Commit with detailed message in editor
git commit

# Stage and commit all tracked files in one command
git commit -am "Quick fix for styling issue"
```

**Viewing History:**
```bash
# View commit history
git log

# Compact one-line view
git log --oneline

# Visual branch diagram
git log --graph --oneline --all

# View specific file history
git log filename.txt

# View changes in each commit
git log -p
```

**Viewing Changes:**
```bash
# See unstaged changes
git diff

# See staged changes
git diff --staged

# Compare branches
git diff main feature-branch

# See changes in specific commit
git show commit-hash
```

### Branching and Merging

**Branch Management:**

```bash
# List all branches
git branch

# Create new branch
git branch feature-login

# Switch to branch
git checkout feature-login

# Create and switch in one command
git checkout -b feature-login

# Modern way (Git 2.23+)
git switch feature-login
git switch -c feature-login

# Delete branch
git branch -d feature-login

# Force delete unmerged branch
git branch -D feature-login

# Rename current branch
git branch -m new-name
```

**Merging:**

```bash
# Merge feature branch into current branch
git checkout main
git merge feature-login

# Merge with commit message
git merge feature-login -m "Integrate login feature"

# Abort merge if conflicts
git merge --abort
```

**Merge Types Visualized:**

```
╔═══════════════════════════════════════════════════════╗
║            🎯 MERGE TYPES 🎯                         ║
╚═══════════════════════════════════════════════════════╝

FAST-FORWARD MERGE (no conflicts, linear history)

    main:     A --- B --- C
                           \
    feature:                D --- E

    After merge:
    main:     A --- B --- C --- D --- E

────────────────────────────────────────────────────────

THREE-WAY MERGE (diverged histories)

    main:     A --- B --- C --- F
                       \       /
    feature:            D --- E

    After merge:
    main:     A --- B --- C --- F --- M
                       \           /
    feature:            D --- E ---

    M = Merge commit combining both branches
```

### Remote Operations

**Working with Remotes:**

```bash
# View remote repositories
git remote -v

# Add a remote
git remote add origin https://github.com/username/repo.git

# Change remote URL
git remote set-url origin https://github.com/username/new-repo.git

# Remove remote
git remote remove origin

# Rename remote
git remote rename origin upstream
```

**Pushing and Pulling:**

```bash
# Push to remote
git push origin main

# Push and set upstream tracking
git push -u origin main

# Push all branches
git push --all

# Force push (DANGEROUS!)
git push --force

# Safer force push
git push --force-with-lease

# Pull changes from remote
git pull origin main

# Pull with rebase instead of merge
git pull --rebase

# Fetch changes without merging
git fetch origin

# View remote branches
git branch -r
```

---

## GitHub: Git in the Cloud

### What is GitHub?

GitHub is a web-based platform that hosts Git repositories and provides collaboration tools:

```
╔════════════════════════════════════════════════════════╗
║              🎯 GITHUB FEATURES 🎯                    ║
╚════════════════════════════════════════════════════════╝

📦 Repository Hosting        🔍 Code Review
   Store code in the cloud      Pull requests & reviews

👥 Collaboration             📊 Project Management
   Teams, permissions           Issues, boards, milestones

🔄 CI/CD Integration         📚 Documentation
   GitHub Actions               README, wikis, Pages

🌟 Social Coding             🔒 Security
   Stars, forks, follows        Dependabot, code scanning

📈 Analytics                 🤖 Automation
   Insights, traffic            Actions, webhooks, apps
```

### GitHub vs Git

```
╔═══════════════════════════════════════════════════════╗
║              GIT vs GITHUB                           ║
╠═══════════════════════════════════════════════════════╣
║ GIT                    │  GITHUB                     ║
╠════════════════════════╪═════════════════════════════╣
║ Version control tool   │  Hosting platform           ║
║ Command-line based     │  Web-based + CLI            ║
║ Works locally          │  Cloud-based                ║
║ Tracks changes         │  Adds collaboration         ║
║ Free and open-source   │  Free + paid tiers          ║
║ Install on computer    │  Account-based service      ║
╚════════════════════════╧═════════════════════════════╝
```

### Key GitHub Features

**1. Pull Requests**

A pull request (PR) is a request to merge your changes into another branch:

```
╔═══════════════════════════════════════════════════════╗
║           🎯 PULL REQUEST WORKFLOW 🎯                ║
╚═══════════════════════════════════════════════════════╝

1. Developer creates feature branch
   $ git checkout -b feature-new-button

2. Makes changes and commits
   $ git add .
   $ git commit -m "Add new button component"

3. Pushes to GitHub
   $ git push origin feature-new-button

4. Opens Pull Request on GitHub
   📝 Describes changes
   👥 Requests reviewers

5. Team reviews code
   💬 Comments on code
   ✅ Approves or requests changes

6. After approval, merge PR
   🎉 Feature integrated into main branch

7. Delete feature branch
   🗑️ Clean up merged branch
```

**2. Issues**

Issues track bugs, features, and tasks:

```markdown
# Example Issue

Title: Add dark mode support

Description:
As a user, I want to toggle between light and dark themes
so that I can use the app comfortably at night.

Acceptance Criteria:
- [ ] Add theme toggle in settings
- [ ] Persist theme choice
- [ ] Update all components to support dark mode

Labels: enhancement, UI
Assignees: @developer
Milestone: v2.0
```

**3. GitHub Actions**

Automate workflows with CI/CD:

```yaml
# .github/workflows/test.yml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: npm test
```

---

## Branching Strategies

### Feature Branch Workflow

The simplest workflow for small teams:

```
╔═══════════════════════════════════════════════════════╗
║        🎯 FEATURE BRANCH WORKFLOW 🎯                 ║
╚═══════════════════════════════════════════════════════╝

main:     A --- B --- C --------------- G --- H
                   \                   /
feature-x:          D --- E --- F ----


Process:
1. Create feature branch from main
2. Develop feature with commits
3. Open pull request
4. Code review and testing
5. Merge back to main
6. Delete feature branch
```

**Commands:**
```bash
# Start feature
git checkout main
git pull origin main
git checkout -b feature-user-profile

# Develop feature
git add .
git commit -m "Add user profile page"
git push origin feature-user-profile

# After PR approval
git checkout main
git merge feature-user-profile
git push origin main
git branch -d feature-user-profile
```

### Git Flow

A more structured workflow for larger projects:

```
╔═══════════════════════════════════════════════════════╗
║              🎯 GIT FLOW MODEL 🎯                    ║
╚═══════════════════════════════════════════════════════╝

main:       A -------------------- F -------- J
            │                      │          │
            │                   [v1.0]     [v1.1]
            │                      │          │
develop:    A --- B --- C --- D -- F -- G -- J
                   \         /         \    /
feature-1:          B1 --- B2           /  /
                             \    /    /  /
feature-2:                    C1 --- C2  /
                                        /
hotfix:                               H


Branch Types:
- main: Production-ready code
- develop: Integration branch for features
- feature/*: New features
- release/*: Prepare releases
- hotfix/*: Emergency production fixes
```

### GitHub Flow

A simplified workflow popular for continuous deployment:

```
╔═══════════════════════════════════════════════════════╗
║            🎯 GITHUB FLOW 🎯                         ║
╚═══════════════════════════════════════════════════════╝

main:  A --- B --- C --- E --- F --- H --- I
                    \       /     \     /
feature:             D ----      G ---

Rules:
1. main is always deployable
2. Create descriptive branches
3. Commit frequently to branch
4. Open PR early
5. Deploy from branch for testing
6. Merge only after review
7. Deploy immediately after merge
```

---

## Collaboration Workflows

### Pull Requests

**Creating Effective Pull Requests:**

```markdown
# Good PR Template

## Description
Brief summary of changes and why they're needed.

## Changes Made
- Added user authentication
- Updated API endpoints
- Fixed mobile responsive issues

## Testing
- [ ] Unit tests pass
- [ ] Manual testing completed
- [ ] Tested on mobile devices

## Screenshots
[Include relevant screenshots]

## Related Issues
Closes #123
Related to #456

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No console logs or debugging code
- [ ] Backward compatible
```

### Code Reviews

**Effective Review Practices:**

```
╔═══════════════════════════════════════════════════════╗
║        🎯 CODE REVIEW BEST PRACTICES 🎯              ║
╚═══════════════════════════════════════════════════════╝

WHAT TO REVIEW:
✅ Correctness: Does it work?
✅ Design: Is it well-structured?
✅ Readability: Is it clear?
✅ Testing: Are there tests?
✅ Documentation: Is it documented?
✅ Performance: Any bottlenecks?
✅ Security: Any vulnerabilities?

HOW TO REVIEW:
💬 Be respectful and constructive
🎯 Focus on the code, not the person
💡 Suggest alternatives
❓ Ask questions rather than commanding
✅ Approve when ready, not perfect
🔍 Review in reasonable chunks
```

**Example Review Comments:**

```
✅ Good:
"Consider using a Map here for O(1) lookups instead of
array.find() which is O(n). This could improve performance
for large datasets."

❌ Bad:
"This is wrong. Use a Map."

────────────────────────────────────────────────────────

✅ Good:
"Nice solution! Have you considered what happens if the
user input is null? We might want to add validation here."

❌ Bad:
"You forgot null checking."
```

### Resolving Merge Conflicts

Conflicts occur when the same part of code is modified in both branches:

```bash
# Attempting to merge
$ git merge feature-branch
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**Conflict Markers in File:**

```javascript
// file.txt
function calculate(x, y) {
<<<<<<< HEAD (current branch)
  return x + y;
=======
  return x * y;
>>>>>>> feature-branch (incoming branch)
}
```

**Resolving Conflicts:**

```bash
# 1. View conflicted files
git status

# 2. Open and edit conflicted files
# Remove conflict markers, choose or combine code

# 3. Mark as resolved
git add file.txt

# 4. Complete the merge
git commit -m "Merge feature-branch and resolve conflicts"

# Alternative: Use merge tool
git mergetool
```

**Preventing Conflicts:**

```
╔═══════════════════════════════════════════════════════╗
║        🎯 PREVENTING MERGE CONFLICTS 🎯              ║
╚═══════════════════════════════════════════════════════╝

1. 🔄 Pull frequently
   Keep your branch updated with main

2. 💬 Communicate
   Coordinate with team on who's editing what

3. 📦 Small commits
   Commit often, smaller changes = fewer conflicts

4. ⚡ Short-lived branches
   Merge feature branches quickly

5. 🎯 Single responsibility
   One feature per branch

6. 🤝 Rebase regularly
   git rebase main (keeps history clean)
```

---

## Visual Representations

### Diagram 1: Git Workflow

```
╔══════════════════════════════════════════════════════════════╗
║              🎯 COMPLETE GIT WORKFLOW 🎯                    ║
╚══════════════════════════════════════════════════════════════╝

WORKING DIRECTORY          STAGING AREA         LOCAL REPO          REMOTE REPO
    (Modified)                (Staged)          (Committed)         (GitHub)

  📝 edit files
       │
       │ git add
       ├─────────────────> 📋 staged
       │                      │
       │                      │ git commit
       │                      ├─────────────> 💾 committed
       │                      │                    │
       │                      │                    │ git push
       │                      │                    └──────────> ☁️ GitHub
       │                      │                                  │
       │                      │                    git fetch     │
       │                      │                 <────────────────┘
       │                      │
       │                      │                    git pull
       │ git checkout/restore │                 <────────────────
       <─────────────────────┘

COMMANDS:
• git add: Stage changes
• git commit: Save to local repo
• git push: Upload to remote
• git pull: Download and merge from remote
• git fetch: Download without merging
• git checkout/restore: Discard changes
```

### Diagram 2: Branching Model

```
╔══════════════════════════════════════════════════════════════╗
║           🎯 BRANCHING AND MERGING 🎯                       ║
╚══════════════════════════════════════════════════════════════╝

Time ──────────────────────────────────────────────────────>

main:        A ─── B ─── C ─────────── H ─── I ─── J
             │           │             │
             │           │          [merge]
             │           │             │
feature-1:   │     D ─── E ─── F ─────┘
             │     │
          [branch] │
                   │
feature-2:         └─── G ─────────────────────> (still open)


Legend:
─── : Commits
│   : Branch point
└── : Branch creation
┘   : Merge point

Each letter (A, B, C...) represents a commit
```

### Diagram 3: Pull Request Flow

```
╔══════════════════════════════════════════════════════════════╗
║         🎯 PULL REQUEST COLLABORATION 🎯                    ║
╚══════════════════════════════════════════════════════════════╝

DEVELOPER                    GITHUB                    TEAM

1. Create branch
   git checkout -b
   feature-login
       │
       ├─────────────────>
       │
2. Make commits              New branch
   git commit                appears
       │                        │
       │                        │
3. Push branch               ┌───┴───┐
   git push              ───>│Branch │
       │                     └───┬───┘
       │                         │
4. Open PR               ┌───────┴────────┐
       │              ───>│  Pull Request  │───>  5. Review
       │                 │   #123          │         code
       │                 │ feature-login   │
       │                 └────────┬────────┘         │
       │                          │                  │
       │                          │        6. Comment/Approve
       │                          │<──────────────────┘
       │                          │
7. Address feedback    8. Tests pass?
   git commit              ┌────┴─────┐
       │                   │   ✓ CI   │
       ├────────────────>  └────┬─────┘
       │                        │
       │                        │
       │                  9. Merge PR
       │                   [Merge]
       │                        │
       │                   ┌────▼─────┐
       │                   │   main   │
       │                   │ updated  │
       │                   └──────────┘
       │
10. Delete branch
    Clean up
```

---

## Best Practices

### Commit Messages

**Anatomy of a Good Commit Message:**

```
Short summary (50 chars or less)

Detailed explanation if needed. Wrap at 72 characters.
Explain WHAT changed and WHY, not HOW (code shows how).

- Bullet points are okay
- Use imperative mood: "Add feature" not "Added feature"
- Reference issues: Fixes #123, Relates to #456
```

**Examples:**

```
✅ Good:
Add user authentication with JWT tokens

Implement JWT-based authentication to secure API endpoints.
Users can now log in and receive a token that expires after
24 hours. This replaces the old session-based auth which was
causing scaling issues.

Fixes #234
```

```
❌ Bad:
fixed stuff

updated some files and changed things
```

**Conventional Commits Format:**

```
type(scope): subject

feat(auth): add JWT token authentication
fix(ui): correct button alignment on mobile
docs(readme): update installation instructions
style(css): format code according to style guide
refactor(api): simplify error handling logic
test(auth): add unit tests for login flow
chore(deps): update dependencies to latest versions
```

### Branch Naming

**Branch Naming Conventions:**

```
╔═══════════════════════════════════════════════════════╗
║          🎯 BRANCH NAMING PATTERNS 🎯                ║
╚═══════════════════════════════════════════════════════╝

PATTERN: <type>/<short-description>

TYPES:
feature/    New features
bugfix/     Bug fixes
hotfix/     Urgent production fixes
release/    Release preparation
docs/       Documentation
test/       Testing
refactor/   Code refactoring

EXAMPLES:
✅ feature/user-authentication
✅ bugfix/login-redirect-issue
✅ hotfix/critical-security-patch
✅ docs/api-documentation
✅ test/add-integration-tests

❌ my-branch
❌ test
❌ new-feature-branch-v2-final
```

### Repository Organization

**Essential Files:**

```
project/
├── .gitignore              # Files Git should ignore
├── README.md               # Project documentation
├── LICENSE                 # License information
├── .github/
│   ├── workflows/          # GitHub Actions
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE.md
├── docs/                   # Additional documentation
├── src/                    # Source code
└── tests/                  # Test files
```

**.gitignore Example:**

```
# .gitignore

# Dependencies
node_modules/
vendor/

# Build outputs
dist/
build/
*.o
*.exe

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Temporary files
tmp/
temp/
```

**README.md Template:**

```markdown
# Project Name

Brief description of what this project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\`\`\`bash
npm install
\`\`\`

## Usage

\`\`\`bash
npm start
\`\`\`

## Contributing

Please read CONTRIBUTING.md for details.

## License

This project is licensed under the MIT License.
```

---

## Common Scenarios and Solutions

### Undoing Changes

**Scenario 1: Undo Unstaged Changes**

```bash
# Discard changes in working directory
git restore file.txt

# Or older syntax
git checkout -- file.txt

# Discard all changes
git restore .
```

**Scenario 2: Unstage Files**

```bash
# Unstage specific file (keep changes)
git restore --staged file.txt

# Or older syntax
git reset HEAD file.txt

# Unstage all files
git restore --staged .
```

**Scenario 3: Undo Last Commit (Keep Changes)**

```bash
# Undo commit, keep changes staged
git reset --soft HEAD~1

# Undo commit, keep changes unstaged
git reset HEAD~1

# Undo commit, discard changes
git reset --hard HEAD~1
```

**Scenario 4: Amend Last Commit**

```bash
# Change last commit message
git commit --amend -m "New message"

# Add forgotten files to last commit
git add forgotten-file.txt
git commit --amend --no-edit
```

**Scenario 5: Revert a Commit (Safe for Public Branches)**

```bash
# Create new commit that undoes changes
git revert commit-hash

# Revert without committing (review first)
git revert --no-commit commit-hash
```

### Stashing Work

Save work temporarily without committing:

```bash
# Stash current changes
git stash

# Stash with description
git stash save "Work in progress on login feature"

# List stashes
git stash list

# Apply most recent stash
git stash apply

# Apply and remove stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Delete specific stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Stash including untracked files
git stash -u
```

**Use Case:**

```bash
# Working on feature, need to fix urgent bug
git stash                   # Save current work
git checkout main           # Switch to main
git checkout -b hotfix-123  # Create hotfix branch
# ... fix bug ...
git commit -m "Fix critical bug"
git checkout feature-branch # Back to feature
git stash pop              # Resume work
```

### Cherry-Picking Commits

Apply specific commits from one branch to another:

```bash
# Apply specific commit to current branch
git cherry-pick commit-hash

# Cherry-pick multiple commits
git cherry-pick commit1 commit2 commit3

# Cherry-pick without committing
git cherry-pick --no-commit commit-hash
```

**Visual Example:**

```
main:     A --- B --- C --- E
                   \
feature:            D --- F --- G

# Want commit F on main
git checkout main
git cherry-pick F

main:     A --- B --- C --- E --- F'
                   \
feature:            D --- F --- G

# F' is a copy of F
```

---

## Advanced Topics

### Rebasing

Rebase rewrites history by moving commits to a new base:

```
╔═══════════════════════════════════════════════════════╗
║             🎯 MERGE VS REBASE 🎯                    ║
╚═══════════════════════════════════════════════════════╝

MERGE (preserves history)

main:     A --- B --- C ------- M
                   \           /
feature:            D --- E ---

Result: New merge commit M

────────────────────────────────────────────────────────

REBASE (rewrites history)

main:     A --- B --- C
                   \
feature:            D --- E

After rebase:

main:     A --- B --- C --- D' --- E'

Result: Linear history, commits D and E rewritten
```

**Rebasing Commands:**

```bash
# Rebase feature branch onto main
git checkout feature-branch
git rebase main

# Interactive rebase (edit commits)
git rebase -i HEAD~3

# Continue after resolving conflicts
git rebase --continue

# Abort rebase
git rebase --abort
```

**⚠️ Golden Rule of Rebasing:**

```
╔═══════════════════════════════════════════════════════╗
║         ⚠️  NEVER REBASE PUBLIC HISTORY ⚠️           ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  ✅ DO rebase:                                        ║
║     • Local branches                                  ║
║     • Branches only you work on                       ║
║     • Before pushing to remote                        ║
║                                                       ║
║  ❌ DON'T rebase:                                     ║
║     • main or master branch                           ║
║     • Shared branches others use                      ║
║     • Commits already pushed to public repo           ║
║                                                       ║
║  Why? Rebasing rewrites commit history,              ║
║  causing issues for others who have those commits.   ║
╚═══════════════════════════════════════════════════════╝
```

### Git Hooks

Automate workflows with Git hooks:

```bash
# Hooks are scripts in .git/hooks/

# Common hooks:
.git/hooks/
├── pre-commit        # Run before commit
├── prepare-commit-msg # Edit commit message
├── commit-msg        # Validate commit message
├── post-commit       # Run after commit
├── pre-push          # Run before push
└── post-merge        # Run after merge
```

**Example pre-commit hook:**

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run tests before committing
npm test

# Check for console.log
if grep -r "console.log" src/; then
    echo "Error: console.log found in code!"
    exit 1
fi

# Format code
npm run format

exit 0
```

### Submodules

Include other Git repositories as subdirectories:

```bash
# Add submodule
git submodule add https://github.com/user/repo.git path/to/submodule

# Clone repo with submodules
git clone --recursive https://github.com/user/main-repo.git

# Update submodules
git submodule update --init --recursive

# Pull changes in submodules
git submodule update --remote
```

---

## Conclusion

Mastering Git and GitHub is essential for modern software development. From basic version control to advanced collaboration workflows, these tools empower developers to work efficiently, maintain code quality, and collaborate seamlessly with teams worldwide.

### Key Takeaways Recap

**Git Fundamentals:**
- Git provides complete version history and change tracking
- The three states (working, staging, committed) give precise control
- Branches enable parallel development without interference

**Collaboration:**
- GitHub extends Git with powerful collaboration features
- Pull requests facilitate code review and team coordination
- Clear communication and good practices prevent conflicts

**Best Practices:**
- Write clear, descriptive commit messages
- Use meaningful branch names
- Keep commits small and focused
- Review code thoughtfully
- Follow team conventions

**Problem Solving:**
- Git provides tools to undo mistakes safely
- Conflicts are normal and manageable
- Stashing helps manage context switching
- Understanding your workflow prevents issues

### Next Steps

1. **Practice Daily:** Use Git for all projects, even personal ones
2. **Explore GitHub:** Contribute to open source, read others' code
3. **Learn Advanced Features:** Rebasing, cherry-picking, bisect
4. **Establish Workflows:** Define team conventions and processes
5. **Automate:** Use hooks and CI/CD for efficiency

Remember: Git mastery comes with practice. Don't fear mistakes—Git's entire purpose is to help you recover from them!

---

## Further Reading

### Official Documentation
- [Git Official Documentation](https://git-scm.com/doc) - Comprehensive Git reference
- [GitHub Guides](https://guides.github.com/) - GitHub feature tutorials
- [Pro Git Book](https://git-scm.com/book/en/v2) - Free complete Git book

### Interactive Learning
- [Learn Git Branching](https://learngitbranching.js.org/) - Visual interactive Git tutorial
- [GitHub Learning Lab](https://lab.github.com/) - Hands-on GitHub courses
- [Git Immersion](http://gitimmersion.com/) - Step-by-step Git tour

### Best Practices
- [Conventional Commits](https://www.conventionalcommits.org/) - Commit message convention
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) - Branching model
- [GitHub Flow](https://guides.github.com/introduction/flow/) - Simplified workflow

### Advanced Topics
- [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) - Automation
- [Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain) - How Git works
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) - Comprehensive tutorials

### Tools
- [GitHub Desktop](https://desktop.github.com/) - GUI for Git
- [GitKraken](https://www.gitkraken.com/) - Visual Git client
- [tig](https://jonas.github.io/tig/) - Text-mode interface for Git

---

**Happy Version Controlling! 🚀**

*This article represents my journey of learning Git and GitHub. I hope it helps you build better software with confidence and collaboration.*
