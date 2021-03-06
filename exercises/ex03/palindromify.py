"""EX03 - palindromify function."""

from typing import Final


__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("red", True))


def palindromify(x: str, y: bool) -> str:
    """Mirroring words."""
    if y is True:
        middle: int = int(len(x) / 2)
        final = (x[1: middle] + x[middle: len])
    else:
        if y is False:
            mid: int = int(len(x) / 2) - 1
            final = (x[1: mid] + x[mid:len])
    return Final
    

if __name__ == "__main__":
    main()