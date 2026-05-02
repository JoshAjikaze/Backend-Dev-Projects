from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR/"issues.json"
USER_DATA_FILE = DATA_DIR/"users.json"

def load_data(filename: str = "issues.json"):
    file_path = DATA_DIR / filename
    if file_path.exists():
        with open(file_path, "r") as f:
            content = f.read()
            if content.strip():
                return json.loads(content)
    return []

def save_data(data, filename: str = "issues.json"):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    file_path = DATA_DIR / filename
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)