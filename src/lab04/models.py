import sys, os
from interfaces import SpecialAction
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lab03.base import Character
from lib.validate import (
    validate_kf_damage,
    validate_block,
    validate_heal,
    validate_health_box,
)


class Character_Boss(Character, SpecialAction):
    def __init__(
        self,
        name,
        health,
        level,
        experience,
        damage,
        kf_damage,
        block=False,
        available=True,
    ):
        validate_kf_damage(kf_damage)
        validate_block(block)
        super().__init__(name, health, level, experience, damage, available)
        self._block = block
        self._kf_damage = kf_damage

    @property
    def kf_damage(self):
        return self._kf_damage

    @property
    def block(self):
        return self._block

    @kf_damage.setter
    def kf_damage(self, value):
        self._kf_damage = validate_kf_damage(value)

    def activate_block(self):
        self._block = True
        return f"{self.name} активировал щит"

    def deactivate_block(self):
        self._block = False
        return f"{self.name} убрал щит"

    def take_damage(self, summ):
        if self._block:
            summ = 0
            return f"{self.name} поставил щит"
        return super().take_damage(summ)

    def ultra_attack(self, target):
        if not isinstance(target, Character):
            raise TypeError("Цель должна быть Character")
        new_damage = int(self.damage * self._kf_damage)
        target.take_damage(new_damage)
        return f"{self.name} в ярости и ударил {target.name} с силой {new_damage}!"
    
    def special_process(self, target):
        return self.ultra_attack(target)
    
    def __str__(self):
        if self._block:
            block = "активирован"
        else:
            block = "деактивирован"
        return super().__str__() + f", щит: {block}"


class Character_Healer(Character, SpecialAction):
    def __init__(
        self, name, health, level, experience, damage, heal, health_box, available=True
    ):
        validate_heal(heal)
        validate_health_box(health_box)
        super().__init__(name, health, level, experience, damage, available)
        self.heal = heal
        self.health_box = health_box

    @property
    def heal(self):
        return self._heal

    @property
    def health_box(self):
        return self._health_box

    @heal.setter
    def heal(self, value):
        self._heal = validate_heal(value)

    @health_box.setter
    def health_box(self, value):
        self._health_box = validate_health_box(value)

    def healing_character(self, target):
        if not isinstance(target, Character):
            raise TypeError("Можно лечить только героев")
        if not target.available:
            raise ValueError(f"{target.name} не активен и не может быть вылечен")
        if self.health_box < self.heal:
            raise ValueError(f"у {self.name} не хватает ресурсов аптечки")
        target.health += self.heal
        self.health_box -= self.heal
        return f"герой {self.name} поделился аптечкой с {target.name} и восстановил {self.heal} здоровья"
    
    
    def special_process(self, target):
        return self.healing_character(target)
        
    
    def __str__(self):
        return (
            super().__str__()
            + f", мощность лечения: {self._heal}, запас аптечки: {self._health_box}"
        )
