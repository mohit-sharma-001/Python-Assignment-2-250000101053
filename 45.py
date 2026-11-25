# Question 45: Write a program to demonstrate the use of the break statement in a loop.

print("Searching for number 5 in range 1..10:")
for num in range(1, 11):
    if num == 5:
        print(f"Found {num}! Breaking loop.")
        break
    print(num, end=" ")
print("\nLoop terminated.")
