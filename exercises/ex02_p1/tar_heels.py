"""Tar Heels exercise redux as a structured program."""

__author__ = "730394883"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(choice: int) -> str: 
    """Tar heel fans function"""
    choice: int = int(input("Enter an int: "))
    if choice % 2 == 0 and choice %7 == 0:
        return "TAR HEELS"
    if choice % 2 == 0:
        return "TAR"
    if choice % 7 == 0:
        return "HEELS"
    return "CAROLINA"


if __name__ == "__main__":
    main()
