"""A vaccination calculator."""

__author__ = "730388741"

from datetime import datetime, timedelta
today: datetime = datetime.today()

population: int = int(input("What is the population? "))
admined: int = int(input("How many dosed have been administered? "))
doses_per_day: int = int(input("How many doses are given per day? "))
target_percent: int = int(input("What is the target percent? "))

vaccinated_ppl: float = admined // 2
vaxed_to_meet_target_percent: float = target_percent / 100 * population

if vaxed_to_meet_target_percent % 2 > 0:
    vaxed_for_target_percent = vaxed_to_meet_target_percent // 1  

vaxed_ppl_per_day: float = doses_per_day / 2
if vaxed_ppl_per_day % 2 > 0:
    vaxed_ppl_per_day = vaxed_ppl_per_day // 1

ppl_to_work_with: float = vaxed_to_meet_target_percent - vaccinated_ppl
days_to_goal1: float = ppl_to_work_with / vaxed_ppl_per_day
if days_to_goal1 % 2 > 0:
    days_to_goal = days_to_goal1 // 1

days_to_goal2: int = (int(days_to_goal1))

datetime = today + timedelta(days_to_goal2)

target_percent1 = str(target_percent)
date_to_goal1 = str(days_to_goal2)

print("We will reach " + target_percent1 + "% " + "vaccination in " + date_to_goal1 + " days, which falls on " + datetime.strftime("%B %d, %Y") + ".")