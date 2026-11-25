# Question 43: Write a program to print a multiplication table from 1 to 10 using nested loops.

print("Multiplication Table (1 to 10):\n")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()
