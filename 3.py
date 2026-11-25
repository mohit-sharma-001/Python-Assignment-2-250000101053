# Question 3: Write a program to calculate the remainder without using the modulus operator.

dividend = 29
divisor = 6

# remainder = dividend - (divisor * quotient)
quotient = dividend // divisor
remainder = dividend - (divisor * quotient)

print(f"Dividend: {dividend}, Divisor: {divisor}")
print("Calculated Remainder:", remainder)
print("Verification with % operator:", dividend % divisor)
