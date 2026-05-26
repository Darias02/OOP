from src.lab07.app import AppManager
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError
from src.lab06.models import Character_Boss, Character_Healer

class CLI:
    
    def __init__(self, app: AppManager) -> None:
        self.app = app

    def run(self) -> None:
        while True:
            self._print_menu()
            try:
                choice = int(input("Выберите пункт меню: "))
                print("-" * 50)
                if choice == 0:
                    print("Сохранение данных и выход из программы...")
                    break
                self._handle_choice(choice)
            except ValueError:
                print("Ошибка: введите корректное число")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")
            print("-" * 50)

    def _print_menu(self) -> None:
        print("\nГлавное меню:")
        print("1. Добавить персонажа")
        print("2. Показать всех персонажей")
        print("3. Найти персонажа по имени")
        print("4. Удалить персонажа")
        print("5. Отфильтровать (по здоровью)")
        print("6. Отсортировать коллекцию")
        print("0. Выход")

    def _handle_choice(self, choice: int) -> None:
        if choice == 1: self._action_add()
        elif choice == 2: self._action_show_all()
        elif choice == 3: self._action_find()
        elif choice == 4: self._action_delete()
        elif choice == 5: self._action_filter()
        elif choice == 6: self._action_sort()
        else: print("Неверный пункт меню")

    def _action_add(self) -> None:
        print("Кого вы хотите добавить? (1 - Босс, 2 - Хилер)")
        type_choice = input("Ваш выбор: ").strip()
        
        try:
            name = input("Имя: ")
            health = int(input("Здоровье: "))
            level = int(input("Уровень: "))
            experience = int(input("Опыт: "))
            damage = int(input("Урон: "))
            
            if type_choice == '1':
                kf_damage = float(input("Коэффициент урона: "))
                block_input = input("Есть блок? (yes/no): ").lower() == 'yes'
                new_char = Character_Boss(name, health, level, experience, damage, kf_damage, block_input)
            elif type_choice == '2':
                heal = int(input("Сила лечения: "))
                health_box = int(input("Кол-во аптечек: "))
                new_char = Character_Healer(name, health, level, experience, damage, heal, health_box)
            else:
                print("Ошибка: Неверный тип.")
                return

            self.app.add_item(new_char)
            print(f"Персонаж '{name}' успешно добавлен!")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except TypeError as e:
            print(f"Ошибка типа данных: {e}")
        except DuplicateItemError as e:
            print(f"Ошибка логики: {e}")

    def _action_show_all(self, items=None) -> None:
        target_items = items if items is not None else self.app.get_all()
        if not target_items:
            print("Коллекция пуста.")
            return
        
        print(f"{'Имя':<15} | {'Тип':<10} | {'Здоровье':<10} | {'Уровень':<8}")
        print("-" * 50)
        for item in target_items:
            role = "Босс" if isinstance(item, Character_Boss) else "Хилер"
            print(f"{item.name:<15} | {role:<10} | {item.health:<10} | {item.level:<8}")

    def _action_find(self) -> None:
        name = input("Введите имя для поиска: ").strip()
        item = self.app.find_by_name(name)
        if item:
            print("\n--- Найден персонаж ---")
            self._action_show_all([item])
        else:
            print("Персонаж не найден.")

    def _action_delete(self) -> None:
        name = input("Введите имя для удаления: ").strip()
        confirm = input(f"Вы точно хотите удалить '{name}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                self.app.delete_item(name)
                print("Успешно удалено.")
            except ItemNotFoundError as e:
                print(f"Ошибка: {e}")
        else:
            print("Удаление отменено.")

    def _action_filter(self) -> None:
        try:
            min_hp = int(input("Введите минимальное количество здоровья: "))
            results = self.app.filter_items(lambda x: x.health >= min_hp)
            print(f"Найдено {len(results)} персонажей:")
            self._action_show_all(results)
        except ValueError:
            print("Ошибка: необходимо ввести число.")

    def _action_sort(self) -> None:
        print("1. По имени")
        print("2. По уровню")
        print("3. По здоровью")
        choice = input("Выберите стратегию: ").strip()
        
        if choice == '1':
            self.app.sort_items(key_func=lambda x: x.name)
        elif choice == '2':
            self.app.sort_items(key_func=lambda x: x.level, reverse=True)
        elif choice == '3':
            self.app.sort_items(key_func=lambda x: x.health, reverse=True)
        else:
            print("Неверный выбор")
            return
        print("Коллекция успешно отсортирована.")
        self._action_show_all()