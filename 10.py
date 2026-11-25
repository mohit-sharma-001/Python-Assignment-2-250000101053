# Question 10: Write a program to calculate the sum of the digits of a two-digit number.

num = 78

tens_digit = num // 10
units_digit = num % 10
digit_sum = tens_digit + units_digit

print(f"Two-digit number: {num}")
print(f"Tens digit: {tens_digit}, Units digit: {units_digit}")
print(f"Sum of digits: {digit_sum}")
