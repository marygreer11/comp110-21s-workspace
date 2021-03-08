"""EX03 - avoid_fifth function."""

__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("I love Taco Tuesday!"))


def avoid_fifth(xs: str) -> str:
    """Taking out the Es."""
    legnth = len(xs)
    location = 0
    letter = "e" and "E"
    while location > legnth:
        if xs[location] == letter:
            xs = xs[:location] + xs[location + 1::]
            legnth -= 1
            location += 1
        else:
            location += 1
    return xs

        
if __name__ == "__main__":
    main()