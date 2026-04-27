import sys, os


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.validate import (
    validate_available,
    validate_damage,
    validate_experience,
    validate_health,
    validate_level,
    validate_name,
)
from interfaces import Action, Printable


class Character(Action, Printable):
    def __init__(self, name, health, level, experience, damage, available=True):
        validate_name(name)
        validate_health(health)
        validate_level(level)
        validate_experience(experience)
        validate_damage(damage)
        validate_available(available)

        self._name = name
        self._health = health
        self._level = level
        self._experience = experience
        self._damage = damage
        self._available = available

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    @property
    def damage(self):
        return self._damage

    @property
    def available(self):
        return self._available

    @name.setter
    def name(self, value):
        validate_name(value)
        self._name = value

    @health.setter
    def health(self, value):
        validate_health(value)
        self._health = value

    @level.setter
    def level(self, value):
        validate_level(value)
        self._level = value

    @experience.setter
    def experience(self, value):
        validate_experience(value)
        self._experience = value

    @damage.setter
    def damage(self, value):
        validate_damage(value)
        self._damage = value

    @available.setter
    def available(self, value):
        validate_available(value)
        self._available = value

    def take_damage(self, summ):
        if not self._available:
            raise ValueError(f"Персонаж {self._name} деактивирован")
        self._health -= abs(summ)

        if self._health <= 0:
            self._health = 0
            self.deactivate()
        return f"{self._name} получил {summ} урона, осталось {self._health} здоровья"

    def gain_experience(self, summ):  # повышение уровня
        if not self._available:
            raise ValueError(f"Персонаж {self._name} деактивирован")
        self._experience += summ
        if self._experience >= 100:
            self._level += self._experience // 100
            self._experience %= 100

    def activate(self):
        self._available = True

    def deactivate(self):
        self._available = False

    def process(self, target):
        result = target.take_damage(self.damage)  # цель теряет здоровье
        self.gain_experience(self.damage)  # атакующий получает опыт
        return result
    
    def to_string(self):
        return str(self)

    def __str__(self):
        status = "доступен" if self._available else "недоступен"
        return f"Персонаж {self._name}: здоровье {self._health}, уровень {self._level}, опыт {self._experience}, урон {self._damage}, статус: {status}"

    def __repr__(self):
        return f"Character(name={self._name}, health={self._health}, level={self._level}, experience={self._experience}, damage={self._damage}, available={self._available})"

    
    def __eq__(self, objectt):
        if not isinstance(objectt, Character):
            return False
        return (
            self._health == objectt._health
            and self._level == objectt._level
            and self._experience == objectt._experience
            and self._damage == objectt._damage
            and self._available == objectt._available
        )
