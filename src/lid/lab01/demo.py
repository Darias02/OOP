from model import Character

def main():
    try:
        c1 = Character(100, 1, 0, 10)
        c2 = Character(100, 1, 0, 10)
        c3 = Character(80, 2, 50, 15, available=False)
        print("Объекты созданы")
    except Exception as e:
        print("Ошибка создания:", e)
        return

    print("\n--- Вывод персонажей ---")
    print(c1)
    print(c2)
    print(c3)


    print("\nСравнение")
    print(f"c1 == c2: {c1 == c2}")
    print(f"c1 == c3: {c1 == c3}")

    print("\nАтрибут класса")
    print(f"Всего создано персонажей: {Character.k_character}")

    print("\nrepr")
    print(repr(c1))

    print("\nИзменение здоровья через сеттер")
    print(f"Здоровье c1 до: {c1.health}")
    c1.health = 80
    print(f"После: {c1.health}")

    print("\nПолучение урона")
    c1.take_damage(30)
    print(c1)

    print("\nПолучение опыта")
    c1.gain_experience(50)
    print(c1)
    c1.gain_experience(70)  # должно повысить уровень
    print(c1)


    print("\nДеактивация персонажа")
    c3.deactivate()
    print(c3)
    try:
        c3.take_damage(10)
    except Exception as e:
        print("Ошибка при попытке нанести урон:", e)

    print("\nАктивация персонажа")
    c3.activate()
    c3.take_damage(10)
    print(c3)

    print("\nПопытка создать персонажа с отрицательным здоровьем")
    try:
        c_bad = Character(-5, 1, 0, 10)
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()