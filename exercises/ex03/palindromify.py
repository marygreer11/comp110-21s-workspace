"""EX03 - palindromify function."""

__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("red", True))


def palindromify(x: str, y: bool) -> str:
    """Mirroring words."""
    if y is True:
        middle: str = x[len(x) - 1 // 2:(len(x) + 2) // 2]
        final: str = (x[1:middle] + x[middle:len])
        return final
    else:
        if y is False:
            mid: str = x[len(x) - 1 // 2:(len(x) + 2) // 2 - 1]
            finalfalse: str = (x[1: mid] + x[mid:len])
            return finalfalse
    


if __name__ == "__main__":
    main()