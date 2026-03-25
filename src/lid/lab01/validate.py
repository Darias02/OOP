def validate_name(value):
    if not isinstance(value, str) or len(value) < 1:
        raise ValueError("Имя должно быть не пустым и строковым значением")


def validate_health(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Здоровье должно быть целым неотрицательным числом")


def validate_level(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Уровень должно быть целым неотрицательным числом")


def validate_experience(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Опыт должен быть целым неотрицательным числом")


def validate_damage(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Урон должен быть целым неотрицательным числом")


def validate_available(value):
    if not isinstance(value, bool):
        raise ValueError("Доступность должна быть True или False")
