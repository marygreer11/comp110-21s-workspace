"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730394883"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    Days: int = days_to_target(population, doses, doses_per_day, target)
    Goal_date: str = future_date(Days)
    print("We will reach", target, "% vaccination in", Days, "days, which falls on", Goal_date)

def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Days until our goal is reached."""
    Goal: int = int(population * (target / 100))
    Days: int = int(((Goal -(doses /2)) / (doses_per_day / 2)))
    return Days


def future_date(Days: int) -> str:
    """Date of target vaccination."""
    today: datetime = datetime.today()
    how_many_days: timedelta = timedelta(Days)
    Date: datetime = today + how_many_days
    Actual_Date: str = Date.strftime("%B %d, %Y")
    return Actual_Date


if __name__ == "__main__":
    main()
