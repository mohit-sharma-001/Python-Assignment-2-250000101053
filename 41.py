# Question 41: Write a program to print the following pattern using nested loops: * / ** / *** / **** / *****.

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
