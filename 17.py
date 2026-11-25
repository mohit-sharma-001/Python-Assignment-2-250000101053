# Question 17: Write a program to check whether a number is even or odd using a bitwise operator.

num = 47

# Using bitwise AND with 1 (last bit is 1 for odd, 0 for even)
if num & 1 == 0:
    print(f"{num} is Even (num & 1 == 0)")
else:
    print(f"{num} is Odd (num & 1 == 1)")
