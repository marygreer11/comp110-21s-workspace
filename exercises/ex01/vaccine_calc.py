"""A vaccination calculator."""

__author__ = "730394883"

from datetime import datetime, time
from datetime import timedelta


Population: int = int(input("The total number of people under consideration..."))
Doses_administered: int = int(input("the total number of vaccine doses already given..."))
Doses_per_day: int = int(input("Total number of doses given each day going forward..."))
Target_percent_vaccinated: int = int(input("What percent of the population is the targetted goal?"))
t1: datetime = datetime.today()
Goal: float = float(Population * (Target_percent_vaccinated / 100))
Days: float = float((Goal - Doses_administered * 1/2) / Doses_per_day)
total: timedelta = timedelta(float(Days) + 1)
print("Population:", Population)
print("Doses Administered:", Doses_administered)
print("Doses Per Day:", Doses_per_day)
print("Target Percent Vaccinated:", Target_percent_vaccinated)
print("We will reach the target % vaccination in") 
print(Days)
print("days.")
