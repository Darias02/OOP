from collection import CharacterCollection
from model import Character

def create_characters():
    c1 = Character("Alice", 100, 3, 50, 20, True)
    c2 = Character("Bob", 80, 1, 10, 10, True)
    c3 = Character("Charlie", 0, 2, 70, 30, False)
    c4 = Character("Dave", 120, 5, 90, 40, True)
    return c1, c2, c3, c4


def main():
    print(f"{paint()}\nДобавление и вывод\n{paint()}")
    collection = CharacterCollection()


    c1, c2, c3, c4 = create_characters()

    collection.add(c1)
    collection.add(c2)
    collection.add(c3)
    collection.add(c4)

    print(f"Все персонажи:")
    for c in collection:
        print(c)

    print(f"\n{paint()}\nПоиск | длина | индексация\n{paint()}")
    print("Длина коллекции:", len(collection))

    print(f"\nЭлемент с индексом 1:")
    print(collection[1])

    print("\nПоиск по имени 'Alice':")
    print(collection.find_by_name("Alice"))
    print("\nПоиск по уровню 1:")
    for c in collection.find_by_level(1):
        print(c)

    print(f"\n{paint()}\nУдаление\n{paint()}")
    collection.remove(c2)
    print("После удаления Bob:")
    for c in collection:
        print(c)

    collection.remove_at(0)
    print("После удаления по индексу 0:")
    for c in collection:
        print(c)

    print(f"\n{paint()}\nСортировка\n{paint()}")
    collection.sort(key=lambda x: x.level)
    print("Отсортировано по уровню:")
    for c in collection:
        print(c)

    print(f"\n{paint()}\nФильтрация\n{paint()}")
    active = collection.get_active()
    print("Активные персонажи:")
    for c in active:
        print(c)

    healthy = collection.more_health(50)
    print("Персонажи со здоровьем > 50:")
    for c in healthy:
        print(c)

    print(f"\n{paint()}\nПроверка дубликатов\n{paint()}")
    try:
        collection.add(Character("Alice", 50, 1, 0, 5))
        print('Персонаж добавлен')
    except ValueError as e:
        print("Ошибка:", e)
    try:
        collection.add(Character("Alice", 50, 1, 0, 5))
        print('Персонаж добавлен')
    except ValueError as e:
        print("Ошибка:", e)

def paint():
    return "-" * 87

main()
