"""EX03 - palindromify function."""

__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("red", True))


def palindromify(x: str, y: bool) -> str:
    """Mirroring words."""
    if y == True:
        middle: str = x[len(x)-1 // 2:(len(x) + 2) // 2]
        final: str = (x[1:middle] + x[middle:len])
    else:
        if y == False:
            middle: str = x[len(x)-1 // 2:(len(x) + 2) // 2 - 1]
            final: str = (x[1: middle] + x[middle:len])
    return final



if __name__ == "__main__":
    main()