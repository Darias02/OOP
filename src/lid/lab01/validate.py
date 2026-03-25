def _validate_name(self, value):
    if not isinstance(value, str) or len(value) < 1:
        raise ValueError("Имя должно быть не пустым и строковым значением")


def _validate_health(self, value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Здоровье должно быть целым неотрицательным числом")


def _validate_level(self, value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Уровень должно быть целым неотрицательным числом")


def _validate_experience(self, value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Опыт должен быть целым неотрицательным числом")


def _validate_damage(self, value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Урон должен быть целым неотрицательным числом")


def _validate_available(self, value):
    if not isinstance(value, bool):
        raise ValueError("Доступность должна быть True или False")
