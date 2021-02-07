"""A vaccination calculator."""

__author__ = "730394883"

from datetime import datetime, date
from datetime import timedelta


Population: int = int(input("The total number of people under consideration..."))
Doses_administered: int = int(input("the total number of vaccine doses already given..."))
Doses_per_day: int = int(input("Total number of doses given each day going forward..."))
Target_percent_vaccinated: int = int(input("What percent of the population is the targetted goal?"))
t1: datetime = datetime.today()
Goal: float = float(Population * (Target_percent_vaccinated / 100))
Days: float = int(((Goal - (Doses_administered / 2)) / (Doses_per_day / 2)))
total: timedelta = timedelta(float(Days))
Date: datetime = t1 + total
future_date: str = Date.strftime("%B %d, %Y") 

print("Population:", Population)
print("Doses Administered:", Doses_administered)
print("Doses Per Day:", Doses_per_day)
print("Target Percent Vaccinated:", Target_percent_vaccinated)
print("We will reach", Target_percent_vaccinated, "% vaccination in", total, "which falls on", future_date)
