# Question 38: Write a program to calculate the sum of digits of a given number.

num = 4567
temp = abs(num)
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

print(f"Number: {num}")
print(f"Sum of digits: {digit_sum}")
