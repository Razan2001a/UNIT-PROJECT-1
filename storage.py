import json
from pathlib import Path

CLIENT_FILE = Path("data/clients.json")
LAWYER_FILE = Path("data/lawyers.json")
CASE_FILE = Path("data/cases.json")


def load_data(file_path):
    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)