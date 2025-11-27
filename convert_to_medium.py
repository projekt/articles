#!/usr/bin/env python3
"""
Convert markdown articles to Medium-friendly text format
Removes YAML frontmatter and keeps Medium-compatible markdown
"""

import os
import re
from pathlib import Path

def convert_markdown_to_medium(input_file, output_file):
    """Convert a markdown file to Medium-friendly format"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Remove the reading time badge if it's on its own line
    content = re.sub(r'\*\*⏱️.*?Minute.*?\*\*\n\n', '', content)

    # Keep the rest as-is since Medium supports markdown
    # Medium will handle: headers, lists, code blocks, links, bold, italic

    # Add a note at the top about canonical URL
    canonical_note = """This article was originally published on my website.
For the latest version and more articles, visit: https://projekt.github.io/articles/

---

"""

    content = canonical_note + content

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Converted: {input_file.name} → {output_file.name}")

def main():
    """Main conversion function"""

    # Create medium directory if it doesn't exist
    medium_dir = Path('medium')
    medium_dir.mkdir(exist_ok=True)

    web_dir = Path('web')

    # List of markdown files to convert
    markdown_files = [
        'git_github_complete_guide.md',
        'dart_null_safety_FINAL_with_TOC.md',
        'programming_paradigms_article.md',
        '01_what_are_programming_paradigms.md',
        '02_imperative_programming.md',
        '03_oop.md',
        '04_functional_programming.md',
        '05_declarative_programming.md',
        '06_procedural_programming.md',
        '07_summary.md',
    ]

    print("Converting markdown files to Medium format...\n")

    for md_file in markdown_files:
        input_path = web_dir / md_file

        if input_path.exists():
            # Change extension to .txt for easy copy-paste
            output_filename = md_file.replace('.md', '.txt')
            output_path = medium_dir / output_filename

            convert_markdown_to_medium(input_path, output_path)
        else:
            print(f"⚠️  File not found: {input_path}")

    print(f"\n✅ Conversion complete! Check the 'medium' directory.")
    print(f"\nTo publish on Medium:")
    print(f"1. Open a .txt file from the medium/ directory")
    print(f"2. Copy all content (Cmd+A, Cmd+C)")
    print(f"3. Paste into Medium's editor")
    print(f"4. Medium will auto-format the markdown")
    print(f"5. Add canonical URL in settings: https://projekt.github.io/articles/[article-name].html")
    print(f"6. Add tags and publish!")

if __name__ == '__main__':
    main()
