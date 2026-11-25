# Question 37: Write a program to count the number of digits in a given integer.

num = 9876543
temp = abs(num)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print(f"Number: {num}")
print(f"Total digits: {count}")
