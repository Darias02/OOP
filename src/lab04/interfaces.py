from abc import ABC, abstractmethod


class Action(ABC):  # выполнить действие
    @abstractmethod
    def process(self, target):
        pass


class SpecialAction(ABC):  # спецавльное действие
    @abstractmethod
    def special_process(self, target):
        pass

class Printable(ABC):
    @abstractmethod
    def to_string(self):
        pass