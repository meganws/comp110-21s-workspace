"""Vaccine calculator exercise as a structured program."""


__author__ = "730388741"

from datetime import datetime, timedelta
today: datetime = datetime.today()


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days1: int = days_to_target(population, doses, doses_per_day, target)
    days2: str = str(days1)
    targetstr: str = str(target)
    date_completed: str = str(future_date(days1))
    print("We will reach " + targetstr + "% " + "vaccination in " + days2 + " days, which falls on " + date_completed + ".")
    return None


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Defining days_to_target."""
    vaccinated_ppl: float = doses // 2
    vaxed_to_meet_target_percent: float = target / 100 * population
    if vaxed_to_meet_target_percent % 2 > 0:
        vaxed_to_meet_target_percent = vaxed_to_meet_target_percent // 1
    ppl_to_work_with: float = vaxed_to_meet_target_percent - vaccinated_ppl
    vaxed_ppl_per_day: float = doses_per_day / 2
    if vaxed_ppl_per_day % 2 > 0:
        vaxed_ppl_per_day = vaxed_ppl_per_day // 1
    days_to_go: float = ppl_to_work_with / vaxed_ppl_per_day
    if days_to_go % 2 > 0:
        days_to_go = int(float(days_to_go // 1))
    days: int = int(days_to_go)
    return days


def future_date(days1: int) -> str:
    """Defining datetime."""
    days: str = str(days_to_target)
    datetime = today + timedelta(days1)
    completion_date: str = str(datetime.strftime("%B %d, %Y"))
    return str(completion_date)


if __name__ == "__main__":
    main()
