import os
import pathlib

project_root = "."

print("=== Project Structure Explorer ===")
for item in sorted(os.listdir(project_root)):
    full_path = os.path.join(project_root, item)
    if item.startswith("."):
        continue
    if os.path.isdir(full_path):
        try:
            n = len([f for f in os.listdir(full_path) if not f.startswith(".")])
            print(f"📁 {item}/ ({n} items)")
        except OSError:
            print(f"📁 {item}/")
    else:
        print(f"📄 {item} ({os.path.getsize(full_path):,} bytes)")

py_files = [
    f for f in pathlib.Path(project_root).rglob("*.py")
    if "venv" not in f.parts
    and ".venv" not in f.parts
    and "__pycache__" not in f.parts
]
print(f"\nTotal .py files (excl. venv): {len(py_files)}")
