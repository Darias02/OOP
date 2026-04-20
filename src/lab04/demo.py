import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab03.base import Character
from lab04.models import Character_Boss, Character_Healer
from lab04.interfaces import Action, SpecialAction

from lib.collection import CharacterCollection



def scenario_actions(collection: CharacterCollection, target: Character):
    print("\n=== СЦЕНАРИЙ 1: ACTION (через коллекцию) ===")
    collection.run_actions(target)


def scenario_special(collection: CharacterCollection, target: Character):
    print("\n=== СЦЕНАРИЙ 2: SPECIAL ACTION (через коллекцию) ===")
    collection.run_special_actions(target)


def scenario_filters(collection: CharacterCollection):
    print("\n=== СЦЕНАРИЙ 3: ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСАМ ===")

    actions = collection.get_actions()
    special = collection.get_special_actions()

    print("\nAction объекты:")
    for obj in actions:
        print(obj.name)

    print("\nSpecialAction объекты:")
    for obj in special:
        print(obj.name)


def scenario_isinstance(collection: CharacterCollection):
    print("\n=== СЦЕНАРИЙ 4: isinstance ===")

    for obj in collection:
        print(
            f"{obj.name}: "
            f"Action={isinstance(obj, Action)}, "
            f"SpecialAction={isinstance(obj, SpecialAction)}"
        )




def scenario_real_actions(hero, boss, healer):
    print("\n=== СЦЕНАРИЙ 5: РЕАЛЬНОЕ ПОВЕДЕНИЕ ===")

    boss.activate_block()
    print(boss.ultra_attack(hero))

    print(healer.healing_character(hero))

    print("\nИтог состояния героя:")
    print(hero)



def main():

    hero = Character("Hero", 100, 1, 0, 10)

    boss = Character_Boss(
        name="Boss",
        health=200,
        level=5,
        experience=0,
        damage=20,
        kf_damage=2.0,
    )

    healer = Character_Healer(
        name="Healer",
        health=80,
        level=3,
        experience=0,
        damage=5,
        heal=30,
        health_box=100,
    )


    collection = CharacterCollection()

    collection.add(hero)
    collection.add(boss)
    collection.add(healer)

    print("\n=== ВСЯ КОЛЛЕКЦИЯ ===")
    for item in collection:
        print(item)

    scenario_actions(collection, hero)
    scenario_special(collection, hero)
    scenario_filters(collection)
    scenario_isinstance(collection)
    scenario_real_actions(hero, boss, healer)
    print(Action)
    print(type(hero).__mro__)

if __name__ == "__main__":
    main()
