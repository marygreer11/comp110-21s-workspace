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
        final: str = (x[1: (len(x) / 2)] + x[(len(x) / 2): len(x)])
    else:
        if y is False:
            final: str = (x[1:((len(x) / 2) - 1)] + x[((len(x) / 2) -1):len])
    return final
    

if __name__ == "__main__":
    main()