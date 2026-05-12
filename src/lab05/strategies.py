"""
strategies.py

Содержит:
- стратегии сортировки
- функции-фильтры
- фабрики функций
- функции для map
- callable-стратегии (паттерн Стратегия)
"""

from models import Character_Boss


def by_name(self):
    return self.name


def by_level(self):
    return self.level


def by_health(self):
    return self.health


def by_level_then_health(self):
    return (self.level, self.health)


# =========================
# 🔽 ФУНКЦИИ-ФИЛЬТРЫ
# =========================

def is_active(self):
    return self.available


def is_high_level(self):
    return self.level > 5


def is_boss(self):
    return isinstance(self, Character_Boss)


# =========================
# 🔽 ФАБРИКА ФУНКЦИЙ
# =========================

def make_health_filter(min_health):
    def filter_fn(self):
        return self.health >= min_health

    return filter_fn


# =========================
# 🔽 ФУНКЦИИ ДЛЯ MAP
# =========================

def to_name(self):
    return self.name


def boost_health(self):
    self.health += 20
    return self


def activate(self):
    self.activate()
    return self


# =========================
# 🔽 CALLABLE-СТРАТЕГИИ
# =========================

class HealStrategy:
    def __call__(self, target):
        target.health += 30
        return target


class DamageBoostStrategy:

    def __call__(self, target):
        target.damage += 10
        return target


class DeactivateStrategy:

    def __call__(self, target):
        target.deactivate()
        return target