# Day 3 - Age Calculator

current_year = int(input("Enter current year: "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print("Your age is:", age)

#other way to find age calculater
from datetime import datetime

current_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print("Your age is:", age)
