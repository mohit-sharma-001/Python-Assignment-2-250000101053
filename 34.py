# Question 34: Write a program to calculate the factorial of a given number using a loop.

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is: {factorial}")
