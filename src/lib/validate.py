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


def validate_heal(heal):
    if not isinstance(heal, int):
        raise TypeError("Сила лечения должна быть целым числом")
    if heal < 0:
        raise ValueError("Сила лечения не может быть отрицательной")
    return heal


def validate_health_box(health_box):
    if not isinstance(health_box, int):
        raise TypeError("Аптечка должна быть целым числом")
    if health_box < 0:
        raise ValueError("Аптечка не может быть отрицательной")
    return health_box


def validate_kf_damage(kf_damage):
    if not isinstance(kf_damage, (int, float)):
        raise TypeError("Коэффициент урона должен быть числом")
    if kf_damage <= 0:
        raise ValueError("Коэффициент урона должен быть больше 0")


def validate_block(block):
    if not isinstance(block, bool):
        raise TypeError("block должен быть bool")
