from pathlib import Path

print("AI Documentation Generator Started")

file = Path("Docs/CHANGELOG.md")

# Create file if it doesn't exist
file.parent.mkdir(exist_ok=True)

if not file.exists():
    file.write_text("# Changelog\n\n")

with open(file, "a", encoding="utf-8") as f:
    f.write("Automatic update from GitHub Actions\n")

print("CHANGELOG updated")
