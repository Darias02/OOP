import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.collection import CharacterCollection
from lab03.base import Character
from lab03.models import Character_Boss, Character_Healer


def create_characters():
    c1 = Character("Alice", 200, 3, 50, 20)
    c2 = Character_Boss("Boss", 200, 10, 1000, 30, kf_damage=2)
    c3 = Character_Healer("Healer", 120, 5, 500, 10, heal=25, health_box=100)
    c4 = Character("Dave", 150, 6, 60, 25)
    return c1, c2, c3, c4


def main():
    print(f"{paint()}\nДобавление и вывод\n{paint()}")
    collection = CharacterCollection()

    c1, c2, c3, c4 = create_characters()
    print(Character)
    print(type(c1))
    collection.add(c1)
    collection.add(c2)
    collection.add(c3)
    collection.add(c4)

    print("Все персонажи:")
    for c in collection:
        print(c)

    print(f"\n{paint()}\nПолиморфизм (process)\n{paint()}")
    target = c1
    for c in collection:
        try:
            print(f"{c.name}: {c.process(target)}")
        except Exception as e:
            print(f"{c.name}: {e}")

    print(f"\n{paint()}\nБой и лечение\n{paint()}")
    print("Босс атакует:")
    print(c2.ultra_attack(c1))
    print(c1)

    print("\nХилер лечит:")
    print(c3.process(c1))
    print(c1)

    print(f"\n{paint()}\nЩит босса\n{paint()}")
    print(c2.activate_block())
    print(c2.take_damage(50))
    print(c2.deactivate_block())
    print(c2.take_damage(50))

    print(f"\n{paint()}\nПроверка типов\n{paint()}")
    for c in collection:
        if isinstance(c, Character_Healer):
            print(f"{c.name} — хилер")
        elif isinstance(c, Character_Boss):
            print(f"{c.name} — босс")
        else:
            print(f"{c.name} — базовый персонаж")

    print(f"\n{paint()}\nФильтрация (через коллекцию)\n{paint()}")

    print("Хилеры:")
    for h in collection.get_only_healers():
        print(h)

    print("\nБоссы:")
    for b in collection.get_only_bosses():
        print(b)

    print(f"\n{paint()}\nПолиморфизм без условий\n{paint()}")
    for c in collection:
        try:
            print(c.process(c1))
        except Exception:
            print(f"{c.name} не выполняет действие")


def paint():
    return "-" * 87


main()
