# Question 25: Write a program to check whether a given year is a leap year.

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
