# Medium Publishing Workflow

This directory contains text versions of all articles, optimized for easy copy-paste into Medium.

## 📁 Available Articles

### Standalone Articles
- `git_github_complete_guide.txt` - Complete Git & GitHub guide (25 min read)
- `dart_null_safety_FINAL_with_TOC.txt` - Dart Null Safety guide (20 min read)
- `programming_paradigms_article.txt` - Programming Paradigms complete (40 min read)

### Programming Paradigms Series (7 parts)
1. `01_what_are_programming_paradigms.txt` - Introduction (4 min)
2. `02_imperative_programming.txt` - Imperative Programming (4 min)
3. `03_oop.txt` - Object-Oriented Programming (5 min)
4. `04_functional_programming.txt` - Functional Programming (7 min)
5. `05_declarative_programming.txt` - Declarative Programming (6 min)
6. `06_procedural_programming.txt` - Procedural Programming (6 min)
7. `07_summary.txt` - Summary & Best Practices (10 min)

## 🚀 How to Publish on Medium

### Step 1: Copy Article Content
```bash
# Open any .txt file from this directory
open git_github_complete_guide.txt

# Or from command line:
cat git_github_complete_guide.txt | pbcopy  # macOS
```

### Step 2: Create New Story on Medium
1. Go to [Medium.com](https://medium.com)
2. Click your profile → "Write"
3. Paste the content (Cmd+V / Ctrl+V)
4. Medium will auto-format the markdown

### Step 3: Set Canonical URL (Important for SEO!)
1. Click "..." (three dots menu)
2. Select "More settings"
3. Under "Advanced settings" → Add canonical link:
   ```
   https://projekt.github.io/articles/[article-name].html
   ```

**Example canonical URLs:**
- Git article: `https://projekt.github.io/articles/git_github_complete_guide.html`
- Null safety: `https://projekt.github.io/articles/dart_null_safety_FINAL_with_TOC.html`
- Programming paradigms: `https://projekt.github.io/articles/programming_paradigms_article.html`
- Series article 1: `https://projekt.github.io/articles/01_what_are_programming_paradigms.html`

### Step 4: Add Tags
Add up to 5 relevant tags for better discoverability:

**For Git article:**
- Git
- GitHub
- Version Control
- Programming
- Developer Tools

**For Dart articles:**
- Dart
- Flutter
- Programming
- Software Development
- Null Safety

**For Paradigms series:**
- Programming
- Software Development
- Dart
- OOP
- Functional Programming

### Step 5: Review and Publish
1. Preview your story
2. Check formatting (especially code blocks and diagrams)
3. Add a featured image (optional)
4. Publish as "Public" or save as "Draft"

## 🔄 Updating Articles

If you update the original markdown files, regenerate Medium versions:

```bash
# From the repository root
python3 convert_to_medium.py
```

This will:
- ✅ Remove YAML frontmatter
- ✅ Add canonical URL notice
- ✅ Keep markdown formatting
- ✅ Create clean .txt files

## 📝 Notes

- **Canonical URLs**: Always set to avoid duplicate content penalties
- **Code blocks**: Medium supports syntax highlighting with triple backticks
- **ASCII diagrams**: May render differently on Medium - review after pasting
- **Images**: Upload separately if needed (Medium doesn't import from markdown)
- **Links**: All internal and external links are preserved
- **Formatting**: Headers, lists, bold, italic, code all work in Medium

## ✨ Tips for Better Medium Engagement

1. **Custom subtitle**: Add a compelling subtitle in Medium editor
2. **Featured image**: Create or use a relevant hero image
3. **First paragraph**: Make it engaging to hook readers
4. **Subheadings**: Medium loves clear section breaks
5. **Call to action**: End with invitation to follow/comment
6. **Respond**: Reply to comments to boost engagement

## 🔗 Original Sources

All articles originally published at:
https://projekt.github.io/articles/

Author: Srđan Ljuština
- Website: https://srdapp.rs
- LinkedIn: https://www.linkedin.com/in/srdjanljustina/
- GitHub: https://github.com/projekt
