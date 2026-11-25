# Question 33: Write a program to calculate the sum of the first N natural numbers.

N = 10
total = 0

for i in range(1, N + 1):
    total += i

print(f"Sum of first {N} natural numbers is: {total}")
