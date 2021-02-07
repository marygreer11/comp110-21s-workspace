"""A vaccination calculator."""

__author__ = "730394883"

from datetime import datetime
from datetime import timedelta


Population: int = int(input("The total number of people under consideration..."))
Doses_administered: int = int(input("the total number of vaccine doses already given..."))
Doses_per_day: int = int(input("Total number of doses given each day going forward..."))
Target_percent_vaccinated: int = int(input("What percent of the population is the targetted goal?"))
today: datetime = datetime.today()

print(Population)
print(Doses_administered)
print(Doses_per_day)
print(Target_percent_vaccinated)
