"""How good are you at guessing?"""

__author__ = "730394883"

from random import randint

def main() -> None:
    """Where program will run."""
    greet()
    cont: int = int(input("Would you like to play the game? Choose 1 to continue or choose 2 to quit. "))
    if cont == 1:
        answer1: int = int(input("What number will the generator give? 1 or 2? "))
        actual1: int = randint(1,2)
        points: int = round1(answer1, actual1)
        moving_on: int = int(input("Would you like to continue to round 2? Press 1 to continue and 2 to quit. "))
        if moving_on == 1:
            answer2: int = int(input("What number will the genorater give? Between 1-10. "))
            actual2: int = randint(1,10)
            points: int = (points)+ (round2(answer2, actual2))
            NAMED_CONSTANT: str = "\U0001f600"
            print(f"Congratulations, you have earned {points} points during the game. Come play again, {NAMED_CONSTANT}, !")
        else:
            if moving_on == 2:
                print("Thank you for stopping by the Ultimate Guessing game! Your session has now ended.")
    else:
        if cont == 2:
            print("Thank you for stopping by the Ultimate Guessing game! Your session has now ended.")


def greet() -> None:
    player: str = str(input("What is your name? "))
    """Greeting the player."""
    print(f"Hello {player}, welcome to the Ultimate Guessing Game!")
    

def round1(answer1: int, actual1: int) -> int:
    """First round of the game."""
    points1: int = 1 or 0
    if answer1 == actual1:
        points1 == 1
        print(f"Congratulations, you have guessed correctly, you have earned, {points1} points this round.")
    else:
        if answer1 != actual1:
            points1 == 0
            print(f"Unfortunately, you have not guessed correctly, you earned, {points1} points this round.")
    return points1


def round2(answer2: int, actual2: int) -> int:
    """Second round of the game."""
    points2: int = 1 or 0 
    if answer2 == actual2:
        points2 = 1
        print(f"Congratulations, you have guessed correctly, you have earned, {points2} points this round.")
    else:
        if answer2 != actual2:
            points2 = 0
            print(f"Unfortunately, you have not guessed correctly. You have earned {points2} points this round.")
    return points2


if __name__ == "__main__":
    main()