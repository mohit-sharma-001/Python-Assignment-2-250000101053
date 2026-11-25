# Question 44: Write a program to print all pairs of numbers from 1 to 5 using nested loops.

print("All pairs (x, y) where x, y in [1..5]:")
for x in range(1, 6):
    for y in range(1, 6):
        print(f"({x}, {y})", end=" ")
    print()
