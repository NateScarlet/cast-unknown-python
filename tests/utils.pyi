from typing import (
    Any, Callable, TypeVar
)
def is_support_encoding(encoding: str) -> bool:    ...


TFunc = TypeVar("TFunc", bound=Callable[..., Any])


def use_encoding(encoding: str) -> Callable[[TFunc], TFunc]:   ...
