# Programmers: Emily Catanzariti, Tim Hunt, and Angel Scott
# Course; CS151, Dr. Rajeev
# Date: 9/23/2021
# Lab Number: 2
# Program Inputs: Number of births, deaths, migrations per second, the current population, and how many years
# Program Outputs: Estimated population for specified amount of years

print("This program will take certain statistics and information to estimate the population of a county in the future.")

# get all input values
births = float(input("How many births per second?"))
deaths = float(input("How many deaths per second?"))
migrations = float(input("How many migrations per second? (If you want to use emigration, enter negative number)."))
current_pop = float(input("What is the current population?"))
years_in_future = float(input("How many years into the future would you like to estimate?"))

# seconds in years
seconds_in_future = years_in_future * 31536000

# total amount for each variable
births_total = births * seconds_in_future
deaths_total = deaths * seconds_in_future
migrations_total = migrations * seconds_in_future

# find total future pop
future_pop = current_pop + births_total - deaths_total + migrations_total

# if pop is neg
if future_pop > 0:
    print("The estimate for the total population is:", future_pop)
else:
    print("Sorry, your population has gone extinct.")
