# Question 8: Write a program to swap two numbers using arithmetic operators.

x = 25
y = 40

print(f"Before swap: x = {x}, y = {y}")

x = x + y  # x becomes 65
y = x - y  # y becomes 25
x = x - y  # x becomes 40

print(f"After swap : x = {x}, y = {y}")
