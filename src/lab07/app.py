from typing import List, Optional, Callable, Any, Dict
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError
from src.lab06.base import Character
from src.lab06.models import Character_Boss, Character_Healer

class AppManager:
    def __init__(self) -> None:
        self._collection: List[Character] = []

    def load_data(self, raw_data: List[Dict[str, Any]]) -> None:
        self._collection.clear()
        for item in raw_data:
            try:
                role = item.get("role")
                if role == "Boss":
                    obj = Character_Boss(
                        name=item["name"], health=item["health"], level=item["level"],
                        experience=item["experience"], damage=item["damage"],
                        kf_damage=item["kf_damage"], block=item["block"], available=item["available"]
                    )
                    self._collection.append(obj)
                elif role == "Healer":
                    obj = Character_Healer(
                        name=item["name"], health=item["health"], level=item["level"],
                        experience=item["experience"], damage=item["damage"],
                        heal=item["heal"], health_box=item["health_box"], available=item["available"]
                    )
                    self._collection.append(obj)
            except Exception:
                pass 
    def get_raw_data(self) -> List[Dict[str, Any]]:
        data = []
        for item in self._collection:
            base_info = {
                "name": item.name, "health": item.health, "level": item.level,
                "experience": item.experience, "damage": item.damage, "available": item.available
            }
            if isinstance(item, Character_Boss):
                base_info.update({"role": "Boss", "kf_damage": item.kf_damage, "block": item.block})
            elif isinstance(item, Character_Healer):
                base_info.update({"role": "Healer", "heal": item.heal, "health_box": item.health_box})
            data.append(base_info)
        return data

    def add_item(self, item: Character) -> None:
        if self.find_by_name(item.name):
            raise DuplicateItemError(f"Персонаж с именем '{item.name}' уже существует.")
        self._collection.append(item)

    def get_all(self) -> List[Character]:
        return self._collection

    def find_by_name(self, name: str) -> Optional[Character]:
        for item in self._collection:
            if item.name.lower() == name.lower():
                return item
        return None

    def delete_item(self, name: str) -> None:
        item = self.find_by_name(name)
        if not item:
            raise ItemNotFoundError(f"Персонаж '{name}' не найден.")
        self._collection.remove(item)

    def filter_items(self, condition: Callable[[Character], bool]) -> List[Character]:
        return [item for item in self._collection if condition(item)]

    def sort_items(self, key_func: Callable[[Character], Any], reverse: bool = False) -> None:
        self._collection.sort(key=key_func, reverse=reverse)