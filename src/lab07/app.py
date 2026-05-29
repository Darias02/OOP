from typing import List, Optional, Any, Dict
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError
from src.lab06.models import Character_Boss, Character_Healer

class AppManager:
    def __init__(self) -> None:
        self._collection: List[Any] = []

    def create_and_add(self, char_type: str, p: Dict[str, Any]) -> None:
        if self.find_by_name(p["name"]):
            raise DuplicateItemError(f"Персонаж '{p['name']}' уже существует")

        if char_type == '1':
            new_char = Character_Boss(
                name=p["name"], health=p["health"], level=p["level"],
                experience=p["experience"], damage=p["damage"],
                kf_damage=p["kf_damage"], block=p["block"]
            )
        elif char_type == '2':
            new_char = Character_Healer(
                name=p["name"], health=p["health"], level=p["level"],
                experience=p["experience"], damage=p["damage"],
                heal=p["heal"], health_box=p["health_box"]
            )
        else:
            raise ValueError("Неверный тип персонажа.")
        
        self._collection.append(new_char)

    def load_from_raw(self, raw_data: List[Dict[str, Any]]) -> None:
        for item in raw_data:
            try:
                role_type = '1' if item.get("role") == "Boss" else '2'
                self.create_and_add(role_type, item)
            except Exception:
                continue

    def get_save_data(self) -> List[Dict[str, Any]]:
        result = []
        for item in self._collection:
            d = {
                "name": item.name, "health": item.health, "level": item.level,
                "experience": item.experience, "damage": item.damage, "available": item.available
            }
            if isinstance(item, Character_Boss):
                d.update({"role": "Boss", "kf_damage": item.kf_damage, "block": item.block})
            else:
                d.update({"role": "Healer", "heal": item.heal, "health_box": item.health_box})
            result.append(d)
        return result

    def get_all(self) -> List[Any]:
        return self._collection

    def find_by_name(self, name: str) -> Optional[Any]:
        for item in self._collection:
            if item.name.lower() == name.lower():
                return item
        return None

    def delete_item(self, name: str) -> None:
        item = self.find_by_name(name)
        if not item:
            raise ItemNotFoundError(f"Персонаж '{name}' не найден")
        self._collection.remove(item)

    def filter_by_hp(self, min_hp: int) -> List[Any]:
        return [item for item in self._collection if item.health >= min_hp]

    def sort_by_strategy(self, attr: str) -> None:
        self._collection.sort(key=lambda x: getattr(x, attr, ""), reverse=(attr != "name"))