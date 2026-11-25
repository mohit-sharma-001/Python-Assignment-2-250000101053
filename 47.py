# Question 47: Write a program to demonstrate the use of the pass statement inside a loop.

print("Demonstrating pass statement inside a loop:")
for i in range(1, 6):
    if i == 3:
        pass  # Placeholder, do nothing
        print("[pass executed at 3]", end=" ")
    else:
        print(i, end=" ")
print()
