# Question 46: Write a program to print numbers from 1 to 20 while skipping multiples of 3 using continue.

print("Numbers from 1 to 20 skipping multiples of 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
