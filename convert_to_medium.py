#!/usr/bin/env python3
"""
Convert markdown articles to HTML for Medium
Generates HTML that can be pasted into Medium's editor
"""

import os
import re
from pathlib import Path

def convert_markdown_to_html(input_file, output_file):
    """Convert a markdown file to HTML"""

    try:
        import markdown
    except ImportError:
        print("❌ Error: markdown library not found!")
        print("Please install it first:")
        print("  pip3 install markdown")
        return False

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove YAML frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=[
        'extra',  # tables, code blocks, etc.
        'codehilite',  # syntax highlighting
        'fenced_code',  # ```code blocks```
        'tables',
        'toc'  # table of contents
    ])

    html_content = md.convert(content)

    # Wrap in proper HTML structure
    canonical_note = """<!-- Original article: https://projekt.github.io/articles/ -->
<div style="background: #f0f0f0; padding: 15px; border-left: 4px solid #333; margin-bottom: 30px;">
<p><strong>Note:</strong> This article was originally published on my website. For the latest version and more articles, visit <a href="https://projekt.github.io/articles/">https://projekt.github.io/articles/</a></p>
</div>

"""

    html_content = canonical_note + html_content

    # Write HTML to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Converted: {input_file.name} → {output_file.name}")
    return True

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

    print("Converting markdown files to HTML for Medium...\n")

    success_count = 0
    for md_file in markdown_files:
        input_path = web_dir / md_file

        if input_path.exists():
            # Change extension to .txt for easy copy-paste
            output_filename = md_file.replace('.md', '.txt')
            output_path = medium_dir / output_filename

            if convert_markdown_to_html(input_path, output_path):
                success_count += 1
        else:
            print(f"⚠️  File not found: {input_path}")

    if success_count > 0:
        print(f"\n✅ Conversion complete! Converted {success_count} files to HTML.")
        print(f"\nTo publish on Medium:")
        print(f"1. Open a .txt file from the medium/ directory")
        print(f"2. Copy all HTML content (Cmd+A, Cmd+C)")
        print(f"3. Go to Medium → Click 'Write'")
        print(f"4. In the editor, paste the HTML code")
        print(f"5. Medium will render it as formatted content")
        print(f"6. Add canonical URL in settings (... menu → More settings)")
        print(f"7. Add tags and publish!")

if __name__ == '__main__':
    main()
