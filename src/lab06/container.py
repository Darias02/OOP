from typing import TypeVar, Generic, Callable, Optional, Protocol
        
class Displayable(Protocol):
    def display(self) -> str:
        ...
class Scorable(Protocol):
    def score(self) -> float:
        ...

T = TypeVar("T")
R = TypeVar("R")
D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]


class Protocol:
    pass

