# Question 20: Write a program to evaluate expressions and demonstrate Python operator precedence.

# Order of precedence: Parentheses, Exponentiation, Unary, Multiplication/Division, Addition/Subtraction, Bitwise, Relational, Logical
result = 100 - 4 * 5 + 3 ** 2 * 2 // 3

print("Expression: 100 - 4 * 5 + 3 ** 2 * 2 // 3")
print("Evaluation order:")
print("  3 ** 2 = 9")
print("  4 * 5 = 20")
print("  9 * 2 = 18")
print("  18 // 3 = 6")
print("  100 - 20 + 6 = 86")
print("Result:", result)
