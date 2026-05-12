from container import TypedCollection, Displayable, Scorable
from base import Character
from models import Character_Boss, Character_Healer


def paint():
    return "-" * 80


def print_section(title: str):
    print(f"\n{paint()}\n {title} \n{paint()}")


def scenario_find(collection: TypedCollection[Character]):
    print_section("Find")

    result1 = collection.find(lambda x: x.name == "Hero")
    result2 = collection.find(lambda x: x.name == "Unknown")

    print("Найдено Hero:", result1)
    print("Не найдено:", result2)


def scenario_filter(collection: TypedCollection[Character]):
    print_section("Filter")

    filtered = collection.filter(lambda x: x.health > 50)

    for item in filtered:
        print(item)


def scenario_map(collection: TypedCollection[Character]):
    print_section("Map")

    names = collection.map(lambda x: x.name)
    levels = collection.map(lambda x: x.level)

    print("Имена:", names)
    print("Уровни:", levels)


def scenario_displayable(collection: TypedCollection[Displayable]):
    print_section("Dicplayable")

    items = collection.map(lambda x: x.display())
    for i in items:
        print(i)


def scenario_scorable(collection: TypedCollection[Scorable]):
    print_section("Scorable")

    scores = collection.map(lambda x: x.score())
    print("Scores:", scores)


def main():
    hero = Character("Hero", 100, 1, 0, 10)

    boss = Character_Boss("Boss", 200, 5, 0, 20, 2.0)

    healer = Character_Healer("Healer", 80, 3, 0, 5, 30, 100)

    collection = TypedCollection[Character]()

    collection.add(hero)
    collection.add(boss)
    collection.add(healer)

    print_section("Collection")
    for item in collection.get_all():
        print(item)

    scenario_find(collection)
    scenario_filter(collection)
    scenario_map(collection)

    display_collection = TypedCollection[Displayable]()
    display_collection.add(hero)
    display_collection.add(boss)

    scenario_displayable(display_collection)

    score_collection = TypedCollection[Scorable]()
    score_collection.add(boss)
    score_collection.add(healer)

    scenario_scorable(score_collection)


if __name__ == "__main__":
    main()
