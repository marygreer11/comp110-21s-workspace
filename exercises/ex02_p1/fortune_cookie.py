"""Fortune cookie exercise redux as a structured program."""

from random import randint
from typing import ForwardRef

__author__ = "730394883"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")
    return None



def fortune_cookie() -> str:
    """Declares fortune"""
    Number: int =randint(1, 100)
    if Number > 50:
     return "You will have a good day"
    if Number < 50:
        return "Your dreams will come true"
    if Number == 50:
     return "Love is in the air"
                
            



# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
