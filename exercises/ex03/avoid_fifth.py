"""EX03 - avoid_fifth function."""

__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("I love Taco Tuesday!"))


def avoid_fifth(xs: str) -> str:
    """Taking out the Es."""
    for letters in xs:
        x: str = xs.translate({ord('e'): ''})
    return x

        
if __name__ == "__main__":
    main()