from src.lab07.app import AppManager
from src.lab07.exceptions import ItemNotFoundError, DuplicateItemError

class CLI:
    
    def __init__(self, app: AppManager) -> None:
        self.app = app

    def run(self) -> None:
        while True:
            self._print_menu()
            try:
                choice = input("Выберите пункт: ").strip()
                print("-" * 55)
                if choice == '0': break
                self._handle_choice(choice)
            except ValueError:
                print("Ошибка: введите число")
            except Exception as e:
                print(f"Ошибка: {e}")
            print("-" * 55)

    def _print_menu(self) -> None:
        print("\n1. Добавить персонажа")
        print("2. Показать всех")
        print("3. Найти по имени")
        print("4. Удалить персонажа")
        print("5. Фильтр по HP")
        print("6. Сортировка")
        print("0. Выход и сохранение")

    def _handle_choice(self, choice: str) -> None:
        if choice == '1': self._action_add()
        elif choice == '2': self._action_show_all()
        elif choice == '3': self._action_find()
        elif choice == '4': self._action_delete()
        elif choice == '5': self._action_filter()
        elif choice == '6': self._action_sort()
        else: print("Неверный пункт.")

    def _action_add(self) -> None:
        print("Тип: 1 - Boss, 2 - Healer")
        t = input("Выбор: ").strip()
        try:
            p = {
                "name": input("Имя: "),
                "health": int(input("Здоровье: ")),
                "level": int(input("Уровень: ")),
                "experience": int(input("Опыт: ")),
                "damage": int(input("Урон: "))
            }
            if t == '1':
                p["kf_damage"] = float(input("Коэффицент урона: ")) 
                p["block"] = input("Блок (yes/no): ").lower() == 'yes' 
            elif t == '2':
                p["heal"] = int(input("Сила лечения: ")) 
                p["health_box"] = int(input("Кол-во аптечек: "))
            
            self.app.create_and_add(t, p)
            print("Успех!")
        except Exception as e:
            print(f"Ошибка валидации: {e}")

    def _action_show_all(self, items=None) -> None:
        target = items if items is not None else self.app.get_all()
        if not target:
            print("Пусто.")
            return
        print(f"{'Имя':<15} | {'Тип':<10} | {'HP':<10} | {'Lvl':<8}")
        print("-" * 55)
        for item in target:
            role = "Boss" if hasattr(item, 'kf_damage') else "Healer"
            print(f"{item.name:<15} | {role:<10} | {item.health:<10} | {item.level:<8}")

    def _action_find(self) -> None:
        name = input("Имя для поиска: ")
        res = self.app.find_by_name(name)
        if res: self._action_show_all([res])
        else: print("Не найден.")

    def _action_delete(self) -> None:
        name = input("Имя для удаления: ")
        if input(f"Удалить {name}? (yes/no): ").lower() == 'yes':
            try:
                self.app.delete_item(name)
                print("Удалено.")
            except ItemNotFoundError as e:
                print(e)

    def _action_filter(self) -> None:
        try:
            hp = int(input("Мин. здоровье: "))
            self._action_show_all(self.app.filter_by_hp(hp))
        except ValueError: print("Ошибка ввода.")

    def _action_sort(self) -> None:
        print("1. По имени, 2. По уровню, 3. По HP")
        m = {'1': 'name', '2': 'level', '3': 'health'}
        c = input("Выбор: ")
        if c in m:
            self.app.sort_by_strategy(m[c])
            self._action_show_all()