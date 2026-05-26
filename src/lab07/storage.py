import json
import os
from typing import List, Dict, Any

def save(collection_data: List[Dict[str, Any]], filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(collection_data, file, ensure_ascii=False, indent=4)

def load(filepath: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []