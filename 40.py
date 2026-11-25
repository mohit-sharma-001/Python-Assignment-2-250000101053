# Question 40: Write a program to print all prime numbers within a given range.

start = 10
end = 50

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()
