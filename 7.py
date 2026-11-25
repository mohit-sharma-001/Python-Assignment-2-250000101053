# Question 7: Write a program to calculate the result of an arithmetic expression using multiple operators.

# Demonstrates evaluation order (PEMDAS)
expr_result = 10 + 5 * 2 ** 3 - (8 / 2) // 2

print("Expression: 10 + 5 * 2 ** 3 - (8 / 2) // 2")
print("Step by step:")
print("  2 ** 3 = 8")
print("  5 * 8 = 40")
print("  (8 / 2) = 4.0")
print("  4.0 // 2 = 2.0")
print("  10 + 40 - 2.0 = 48.0")
print("Computed result:", expr_result)
