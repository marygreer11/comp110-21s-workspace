"""An exercise in remainders and boolean logic."""

__author__ = "730394883"


x: int = int(input("Enter an int: "))

if x % 2== 0:
    print("TAR")
else:
    if x % 7== 0:
        print("HEELS")
    else:
        print("CAROLINA")

