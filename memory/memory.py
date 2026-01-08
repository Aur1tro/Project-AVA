from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory", "log.txt")

def save_memory(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

def recall_memory(limit=5):
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return lines[-limit:] if lines else []
    except FileNotFoundError:
        return []
