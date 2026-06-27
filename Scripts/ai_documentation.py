#print("AI Documentation Generator Started")
from pathlib import Path

print("AI Documentation Generator Started")

docs = Path("Docs")

for file in docs.glob("*.md"):
    print(file.name)

print("Completed")
