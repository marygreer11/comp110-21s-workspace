"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394883"


from random import randint


Fortune: int = int(randint(1, 100)) 

print("Your fortune cookie says...")

if Fortune < 30:
    print("You will have a great week.")
else: 
    if Fortune < 50:
        print("You will be productive this month.")
    else:
        if Fortune > 70:
            print("You will find money soon.")
        else:
            print("You will make a huge discovery soon.")

print("Now, go spread positive vibes!")