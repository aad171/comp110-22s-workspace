"""An Example of Union Types."""

from typing import Union


def log(info: Union[int, str]) -> None:
    """log is a function that can be called with _either_ an int or a str argument."""
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("Hello, World")
log(110)