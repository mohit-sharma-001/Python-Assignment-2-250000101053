# Question 16: Write a program to demonstrate left-shift and right-shift operators.

num = 8  # Binary: 1000

# Left shift (num * 2^n)
left_shifted = num << 2
# Right shift (num // 2^n)
right_shifted = num >> 2

print(f"Original: {num} (bin: {bin(num)})")
print(f"num << 2: {left_shifted} (bin: {bin(left_shifted)})")
print(f"num >> 2: {right_shifted} (bin: {bin(right_shifted)})")
