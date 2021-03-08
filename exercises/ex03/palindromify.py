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
        x2: str = str(x)[:: - 1]
        final: str = x + x2
    else:
        if y is False:
            x3: str = (str(x)[:: - 1])
            x4: str = x3.replace(x3[0], "")
            final: str = x + x4
    return final
    

if __name__ == "__main__":
    main()