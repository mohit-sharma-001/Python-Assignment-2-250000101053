# Question 50: Write a program to print the following pattern using nested loops: ***** / **** / *** / ** / *.

rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
