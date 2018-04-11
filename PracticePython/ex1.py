# Coded to run in python 3
import datetime
from dateutil.relativedelta import relativedelta

print("This program will calculate the year you are going to turn 100 years old")

print("Please enter your name: ", end=' ')
name = input()
print("Please enter your age: ",  end=' ')
age= int(input())

turn_hundred_date = (datetime.datetime.now() - relativedelta(years = age)) + relativedelta(years = 100)

print(f"Dear {name}, you'll be 100 years old on {turn_hundred_date}")
