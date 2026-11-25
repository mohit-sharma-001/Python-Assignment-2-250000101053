# Question 35: Write a program to print the multiplication table of a given number.

num = 7
print(f"Multiplication Table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i:2d} = {num * i}")
