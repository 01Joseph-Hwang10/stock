from typing import Any, Callable, Generic, List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

class Array(Generic[T]):

    source: List[T]

    def __init__(self, source: List[T]) -> None:
        self.source = source

    def map(self, cb: Callable[[T], U]):
        return Array([cb(item) for item in self.source])

    def filter(self, cb: Callable[[T], bool]):
        return Array([item for item in self.source if cb(item)])
