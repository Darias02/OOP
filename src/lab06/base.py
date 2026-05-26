import sys, os


'''sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.validate import (
    validate_available,
    validate_damage,
    validate_experience,
    validate_health,
    validate_level,
    validate_name,
)
from lab05.interfaces import Action, Printable
'''
from src.lib.validate import validate_available, validate_damage, validate_experience, validate_health, validate_level, validate_name
from src.lab05.interfaces import Action, Printable

class Character(Action, Printable):
    def __init__(
        self,
        name: str,
        health: int,
        level: int,
        experience: int,
        damage: int,
        available: bool = True,
    ) -> None:
        validate_name(name)
        validate_health(health)
        validate_level(level)
        validate_experience(experience)
        validate_damage(damage)
        validate_available(available)

        self._name: str = name
        self._health: int = health
        self._level: int = level
        self._experience: int = experience
        self._damage: int = damage
        self._available: bool = available

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @property
    def level(self) -> int:
        return self._level

    @property
    def experience(self) -> int:
        return self._experience

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def available(self) -> bool:
        return self._available

    @name.setter
    def name(self, value: str) -> None:
        validate_name(value)
        self._name = value

    @health.setter
    def health(self, value: int) -> None:
        validate_health(value)
        self._health = value

    @level.setter
    def level(self, value: int) -> None:
        validate_level(value)
        self._level = value

    @experience.setter
    def experience(self, value: int) -> None:
        validate_experience(value)
        self._experience = value

    @damage.setter
    def damage(self, value: int) -> None:
        validate_damage(value)
        self._damage = value

    @available.setter
    def available(self, value: bool) -> None:
        validate_available(value)
        self._available = value

    def take_damage(self, summ: int) -> str:
        if not self._available:
            raise ValueError(f"Персонаж {self._name} деактивирован")
        self._health -= abs(summ)

        if self._health <= 0:
            self._health = 0
            self.deactivate()
        return f"{self._name} получил {summ} урона, осталось {self._health} здоровья"

    def gain_experience(self, summ: int) -> None:
        if not self._available:
            raise ValueError(f"Персонаж {self._name} деактивирован")
        self._experience += summ
        if self._experience >= 100:
            self._level += self._experience // 100
            self._experience %= 100

    def activate(self) -> None:
        self._available = True

    def deactivate(self) -> None:
        self._available = False

    def process(self, target: "Character") -> str:
        result = target.take_damage(self.damage)
        self.gain_experience(self.damage)
        return result

    def to_string(self) -> str:
        return str(self)

    def display(self) -> str:
        return str(self)

    def __str__(self) -> str:
        status = "доступен" if self._available else "недоступен"
        return f"Персонаж {self._name}: здоровье {self._health}, уровень {self._level}, опыт {self._experience}, урон {self._damage}, статус: {status}"

    def __repr__(self) -> str:
        return f"Character(name={self._name}, health={self._health}, level={self._level}, experience={self._experience}, damage={self._damage}, available={self._available})"

    def __eq__(self, objectt: object) -> bool:
        if not isinstance(objectt, Character):
            return False
        return (
            self._health == objectt._health
            and self._level == objectt._level
            and self._experience == objectt._experience
            and self._damage == objectt._damage
            and self._available == objectt._available
        )
