from abc import ABC, abstractmethod





class Action(ABC): #выполнить действие
    @abstractmethod
    def process(self, target):
        pass

'''class Affectable(ABC): #принять на себя эффект (урон)
    @abstractmethod
    def take_effect(self, value):
        pass'''

class SpecialAction(ABC): #спецавльное действие
    @abstractmethod
    def special_process(self, target):
        pass
