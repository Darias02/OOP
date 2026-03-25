from model import Character


def main():
    print(f"{paint()}\nСоздание объектов\n{paint()}\n")
    p1, p2, p3, p4 = create_character()
    print(f"\n\n{paint()}\nВывод repr\n{paint()}\n")
    reprr(p3)
    print(f"\n\n{paint()}\nСравнение\n{paint()}\n")
    test_eq(p1, p4, p3)
    print(f"\n\n{paint()}\nИзменение состояния персонажей\n{paint()}\n")
    change_available(p2, p3)
    print(f"\n\n{paint()}\nИзменение здоровья через setter\n{paint()}\n")
    test_setter(p1)
    print(
        f"\n\n{paint()}\nБой между персонажами {p1.name} и {p3.name}\n{paint()}\n\n<Данные>\n{p1}\n{p3}"
    )
    battle(p1, p3)
    print(f"\n\n{paint()}\nСоздание некорректного персонажа\n{paint()}\n")
    bad_character()


def create_character():
    try:
        p1 = Character("Kai", 100, 0, 50, 55)
        print(p1)
        p2 = Character("Shadow", 30, 0, 10, 5)
        print(p2)
        p3 = Character("Venom", 80, 2, 50, 77, available=False)
        print(p3)
        p4 = Character("Kai", 100, 0, 50, 55)
        print(p4)
    except Exception as e:
        print("Ошибка создания:", e)
        return

    return p1, p2, p3, p4


def battle(p1, p3):
    if not p1.available or not p3.available:
        raise ValueError("Персонаж деактивирован")
    lvl = p3.level
    exp = p3.experience

    print(f"\n- Получение урона персонажем {p1.name} от персонажа {p3.name}")
    print(f"{p1.name}: здоровье {p1.health} ->", end=" ")
    p1.take_damage(p3.damage)
    print(p1.health)
    print(f"- Повышение показателей {p3.name}")
    p3.gain_experience(p3.damage)
    print(f"{p3.name}: уровень {lvl} -> {p3.level}, опыт {exp} -> {p3.experience}")
    print("- Итог боя")

    print(p1)
    print(p3)


def reprr(p3):
    print(repr(p3))


def test_setter(p1):
    print(f"Здоровье {p1.name} до изменения: {p1.health}")
    try:
        p1.health = 80
    except Exception as e:
        print(e)
    print(f"После: {p1.health}")


def test_eq(p1, p4, p3):
    print(f"{p1.name} == {p4.name}: {p1 == p4}")
    print(f"{p1.name} == {p3.name}: {p1 == p3}")


def change_available(p2, p3):
    print(f"{p3.name}:")
    print(p3.available, "->", end=" ")
    p3.activate()
    print(p3.available)
    print(f"{p2.name}:")
    print(p2.available, "->", end=" ")
    p2.deactivate()
    print(p2.available)


def bad_character():
    try:
        p4 = Character("Bad", -30, 5, 60, 20)
    except Exception as e:
        print("Ошибка создания:", e)


def paint():
    return "-" * 87


main()
