import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from model import Character
from lab01.validate import (
    validate_available,
    validate_damage,
    validate_experience,
    validate_health,
    validate_level,
    validate_name,
)


class CharacterCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Character):
            raise TypeError("Можно добавлять только Character")
        if self.find_by_name(item.name) is not None:
            raise ValueError(
                f"Персонаж с именем '{item.name}' уже существует в коллекции"
            )
        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError('Элемент не найден')
        self._items.remove(item)

    def get_all(self):
        return self._items.copy

    def find_by_level(self, search):
        return [character for character in self._items if character.level == search]

    def find_by_name(self, search):
        for character in self._items:
            if character.name == search:
                return(character)
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона (0-{len(self._items)-1})")
        return self._items[index]

    def remove_at(self, index):
        return self._items.pop(index)
    
    def sort(self, key):
        self._items.sort(key=key)

    def get_active(self):
        collection_2 = CharacterCollection()
        for i in self._items:
            if i.available:
                collection_2.add(i)
        return collection_2
    def more_health(self, min_health):
        collection_m_h = CharacterCollection()
        for i in self._items:
            if i.health > min_health:
                collection_m_h.add(i)
        return collection_m_h