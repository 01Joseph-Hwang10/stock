from typing import Any, Callable

def safely_index(getter: Callable, ifNull: Any) -> Any:
    try:
        return getter()
    except IndexError:
        return ifNull

def as_bool(value: Any) -> bool:
    return True if value != None else False
