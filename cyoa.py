"""How good are you at guessing?"""

__author__ = "730394883"

from random import randint
def main() -> None:
    greet
    cont: int = int(input("Would you like to play the game? Choose 1 to continue or choose 2 to quit. "))
    if cont == 1:
        round1
        moving_on: int = int(input("Would you like to continue to round 2? Press 1 to continue and 2 to quit. "))
        if moving_on == 1:
            round2
        else:
            if moving_on == 2:
                print("Thank you for stopping by the Ultimate Guessing game! Your session has now ended.")
    else:
        if cont == 2:
            print("Thank you for stopping by the Ultimate Guessing game! Your session has now ended.")
    return None

def greet() -> None:
    """Greeting the player"""
    player: str = str(input("What is your name? "))
    print(f"Hello {player}, welcome to the Ultimate Guessing Game!")
    return None

def round1(Answer: int, Actual: int) -> int:
    """First round of the game."""
    answer1: int = int(input("What number will the genorator give? 1 or 2? "))
    actual1: int = randint(1,2)
    points: int = 1 or 0
    if answer1 == actual1:
        print("Congratulations, you have guessed correctly, you now have 1 point.")
        points: int = 1
    else:
        if answer1 != actual1:
            print("Unfortunately, you have not guessed correctly, you did not earn a point.")
            points: int = 0
    return points

def round2(Answer: int, Actual: int) -> int:
    """Second round of the game."""
    answer2: int = int(input("What number will the genorater give? Between 1-10. "))
    actual2: int = randint(1,10)
    points2: int = 1 or 0 
    if answer2 == actual2:
        print("Congratulations, you have guessed correctly, you have earned 1 point.")
        points2: int = 1
    else:
        if answer2 != actual2:
            print("Unfortunately, you have not guessed correctly. You did not earn a point this round.")
            points2: int = 0
    return points2
    




















if __name__ == "__main__":
    main()
    