# Question 24: Write a program to find the greatest among three numbers.

a = 34
b = 67
c = 52

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print(f"Numbers: a = {a}, b = {b}, c = {c}")
print(f"The greatest number is: {greatest}")
