import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from lib.lab01.model import Character
from lib.lab01.validate import validate_available, validate_damage, validate_experience, validate_health, validate_level, validate_name

class CharacterCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Character):
            raise TypeError("Можно добавлять только Character")
        self._items.append(item)

    def remove(self, item):
        if item in self._items:
            self._items.remove(item)

    def get_all(self):
        return self._items