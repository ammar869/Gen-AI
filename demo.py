from pathlib import Path

# Change this path if you want another location
base_path = Path.home() / "Documents" / "GenAI-LangChain"

folders = [
    "01-Notes",
    "02-Code",
    "03-Mini-Projects",
    "04-Cheat-Sheets",
    "05-Resources",
    "05-Resources/PDFs",
    "05-Resources/Images",
]

# Create folders
for folder in folders:
    (base_path / folder).mkdir(parents=True, exist_ok=True)

# Create README.md
readme = base_path / "README.md"

if not readme.exists():
    readme.write_text(
"""# GenAI-LangChain

This repository contains my LangChain learning journey.

## Folder Structure

- 01-Notes
- 02-Code
- 03-Mini-Projects
- 04-Cheat-Sheets
- 05-Resources

Goal: Become a professional AI Engineer by building projects.
""",
    encoding="utf-8"
    )

print(f"✅ Project structure created at:\n{base_path}")