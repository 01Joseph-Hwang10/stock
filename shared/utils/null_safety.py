from typing import Any, Callable

def safely_index(getter: Callable, ifNull: Any) -> Any:
    try:
        return getter()
    except IndexError:
        return ifNull
