class Character:
    k_character = 0
    def _validate_health(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Здоровье должно быть целым неотрицательным числом")

    def _validate_level(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Уровень должен быть целым числом >= 1")

    def _validate_experience(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Опыт должен быть целым неотрицательным числом")

    def _validate_damage(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Урон должен быть неотрицательным числом")

    def _validate_available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Доступность должна быть True или False")
    
    
    def __init__(self, health, level, experience, damage, available=True):
        self._validate_health(health)
        self._validate_level(level)
        self._validate_experience(experience)
        self._validate_damage(damage)
        self._validate_available(available)
        Character.k_character += 1
        self._health = health
        self._level = level
        self._experience = experience
        self._damage = damage
        self._available = available


    @property
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
    
    def __str__(self):
        status = "доступен" if self._available else "недоступен"
        return (f"Персонаж: здоровье {self._health}, уровень {self._level}, опыт {self._experience}, урон {self._damage}, статус: {status}")
    def __eq__(self, objectt):
        if isinstance(objectt, Character) == False:
            return False
        return (self._health == objectt._health and self._level == objectt._level and self._experience == objectt._experience and self._damage == objectt._damage and self._available == objectt._available)
    
    def __repr__(self):
        return f"Character(health={self._health}, level={self._level}, experience={self._experience}, damage={self._damage}, available={self._available})"
        


    def take_damage(self, summ):
        if not isinstance(summ, (int, float)) or summ <0:
            raise ValueError("Здоровье должно быть неотрицательным числом")
        if not self._available:
            raise Exception('Персонаж не доступен')
        self._health -= summ 
        if self._health < 0:
            self._health = 0
    def gain_experience(self, summ):
        if not isinstance(summ, int) or summ <0:
            raise ValueError("Опыт должен быть целым неотрицательным числом")
        if not self._available:
            raise Exception('Персонаж не доступен')
        self._experience += summ
        while self._experience >= 100:
            self._experience -= 100
            self._level += 1
            print(f"Уровень повышен! Текущий уровень: {self._level}")
    
    def activate(self):
        self._available = True

    def deactivate(self):
        self._available = False





