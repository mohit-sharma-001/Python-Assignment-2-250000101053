# Question 6: Write a program to demonstrate the difference between / and // operators.

a = 15
b = 4

float_div = a / b
floor_div = a // b

print(f"a = {a}, b = {b}")
print("Using / (Floating-point division):", float_div, f"(Type: {type(float_div).__name__})")
print("Using // (Floor/Integer division) :", floor_div, f"(Type: {type(floor_div).__name__})")
