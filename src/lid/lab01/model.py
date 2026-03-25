class Character:
    def __init__(self, name, health, level, experience, damage, available=True):
        self._validate_name(name)
        self._validate_health(health)
        self._validate_level(level)
        self._validate_experience(experience)
        self._validate_damage(damage)
        self._validate_available(available)

        self._name = name
        self._health = health
        self._level = level
        self._experience = experience  # опыт
        self._damage = damage  # урон
        self._available = available

    @property
    def name(self):
        return self._name

    @property  # чтобы вне класса юыло удобнее обращаться
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    @property
    def damage(self):
        return self._damage

    @property
    def available(self):
        return self._available

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @health.setter
    def health(self, value):
        self._validate_health(value)
        self._health = value

    @level.setter
    def level(self, value):
        self._validate_level(value)
        self._level = value

    @experience.setter
    def experience(self, value):
        self._validate_experience(value)
        self._experience = value

    @damage.setter
    def damage(self, value):
        self._validate_damage(value)
        self._damage = value

    @available.setter
    def available(self, value):
        self._validate_available(value)
        self._available = value

    def _validate_name(self, value):
        if not isinstance(value, str) or len(value) < 1:
            raise ValueError("Имя должно быть не пустым и строковым значением")

    def _validate_health(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Здоровье должно быть целым неотрицательным числом")

    def _validate_level(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Уровень должно быть целым неотрицательным числом")

    def _validate_experience(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Опыт должен быть целым неотрицательным числом")

    def _validate_damage(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Урон должен быть целым неотрицательным числом")

    def _validate_available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Доступность должна быть True или False")

    def take_damage(self, summ):  # получение урона
        self._health -= abs(summ)
        if self._health <= 0:  # если здоровье отрицательное то персонаж деактивируется
            self._health = 0
            self._available = False

    def gain_experience(self, summ):  # получение опыта и нанесение урона
        self._experience += summ
        if self._experience >= 100:  # получение опыта и повышение уровня
            self._level += self._experience // 100
            self._experience %= 100

    def __str__(self):
        status = "доступен" if self._available else "недоступен"
        return f"Персонаж {self._name}: здоровье {self._health}, уровень {self._level}, опыт {self._experience}, урон {self._damage}, статус: {status}"

    def __repr__(self):
        return f"Character(name ={self._name}, health={self._health}, level={self._level}, experience={self._experience}, damage={self._damage}, available={self._available})"

    def __eq__(self, objectt):
        if not isinstance(objectt, Character):
            return False
        return (
            self._health == objectt._health
            and self._level == objectt._level
            and self._experience == objectt._experience
            and self._damage == objectt._damage
            and self._available == objectt._available
        )
