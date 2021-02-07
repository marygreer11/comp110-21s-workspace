"""A vaccination calculator."""

__author__ = "730394883"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
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
