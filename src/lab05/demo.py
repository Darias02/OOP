from collection import CharacterCollection
from base import Character
from models import Character_Boss, Character_Healer

from strategies import (
    by_name,
    by_level,
    by_health,
    is_active,
    is_high_level,
    is_boss,
    make_health_filter,
    boost_health,
    HealStrategy,
)


def print_collection(title, collection):
    print(f"\n -> {title} ")
    for item in collection:
        print(item)


def main():
    collection = CharacterCollection()

    # создаём персонажей
    c1 = Character("Alice", 100, 3, 50, 10)
    c2 = Character("Bob", 150, 6, 20, 15)
    c3 = Character_Boss("Dragon", 300, 10, 0, 30, 2)
    c4 = Character_Healer("Priest", 120, 4, 40, 5, 20, 100)
    c5 = Character("Eve", 80, 2, 10, 8)

    for c in [c1, c2, c3, c4, c5]:
        collection.add(c)

    print_collection("Исходная коллекция", collection)
    print(f"\n{paint()}\nцепочка\n{paint()}")
    collection.filter_by(is_active)
    collection.sort_by(by_level)
    collection.apply(boost_health)

    print_collection("После filter, sort, apply", collection)

    print(f"\n{paint()}\nразные сортировки\n{paint()}")
    collection.sort_by(by_name)
    print_collection("Сортировка по имени", collection)

    collection.sort_by(by_health)
    print_collection("Сортировка по здоровью", collection)
    print(f"\n{paint()}\ncallable\n{paint()}")
    heal = HealStrategy()
    collection.apply(heal)

    print_collection("После HealStrategy", collection)

    print(f"\n{paint()}\nmap\n{paint()}")
    names = list(map(lambda x: x.name, collection))
    print(names)
    print(f"\n{paint()}\nfilter\n{paint()}")
    filtered = list(filter(is_high_level, collection))
    for item in filtered:
        print(item)
    print(f"\n{paint()}\nфабрика\n{paint()}")
    custom_filter = make_health_filter(150)
    collection.filter_by(custom_filter)

    print_collection("Здоровье >= 150", collection)

def paint():
    return "-" * 87

if __name__ == "__main__":
    main()