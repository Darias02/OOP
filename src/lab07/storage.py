import json
import os
from typing import List, Dict, Any

def save(collection, filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(collection, file, ensure_ascii=False, indent=4)

def load(filepath: str) -> list:
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []