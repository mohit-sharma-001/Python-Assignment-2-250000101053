# Question 36: Write a program to reverse a given integer using a while loop.

num = 12345
original = num
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10

print(f"Original Number: {original}")
print(f"Reversed Number: {reversed_num}")
