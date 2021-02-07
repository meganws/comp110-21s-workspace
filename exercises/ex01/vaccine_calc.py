"""A vaccination calculator."""

__author__ = "730388741"

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



# Begin your solution here...
from datetime import datetime, timedelta
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
fortnight: timedelta = timedelta(7+7)
future: datetime = today + fortnight

population: int = int(input("What is the population? "))
admined: int = int(input("How many dosed have been administered? "))
doses_per_day: int = int(input("How many doses are given per day? "))
target_percent: int = int(input("What is your target percent? "))

vaccinated_ppl: float = admined // 2
vaxed_to_meet_target_percent: float = target_percent / 100 * population

if vaxed_to_meet_target_percent % 2 > 0:
    vaxed_for_target_percent = vaxed_to_meet_target_percent // 1  

#using "// 1" rounds down since you can't have .2 of a person

vaxed_ppl_per_day: float = doses_per_day / 2
if vaxed_ppl_per_day % 2 > 0:
    vaxed_ppl_per_day = vaxed_ppl_per_day // 1

days_to_goal1: float =  (vaxed_to_meet_target_percent - vaccinated_ppl) / vaxed_ppl_per_day

days_to_goal2: int = int(days_to_goal1)


date_goal_reached: datetime = today + timedelta(days_to_goal2)

target_percent1 = str(target_percent)
date_to_goal1 = str(days_to_goal2)
#date_goal_reached.strftime("%B %d, %Y")

print("We will reach " + target_percent1 + "% " + "vaccination in " + date_to_goal1 + " days, which falls on " + date_goal_reached.strftime("%B %d, %Y") + ".")
#find a way to get from total vax ppl to days



#days_left is the number of days it will take to get all the unxed ppl vaccinated
#no wait we're going for a target percent not everyone getting vaccined
#target percent will be __ / 100 = target_percent? maybe not?

#do timedelta(some calculation)