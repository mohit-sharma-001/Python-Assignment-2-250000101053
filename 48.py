# Question 48: Write a program to demonstrate the else clause of a for loop.

numbers = [2, 4, 6, 8, 10]
target = 5

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was not found in the list (else clause executed).")
