# Question 30: Write a program to calculate electricity charges using different slabs with nested if statements.

units = 250
bill = 0.0

if units <= 100:
    bill = units * 1.50
else:
    bill += 100 * 1.50
    if units <= 200:
        bill += (units - 100) * 2.50
    else:
        bill += 100 * 2.50
        if units <= 300:
            bill += (units - 200) * 4.00
        else:
            bill += 100 * 4.00
            bill += (units - 300) * 5.00

print(f"Units consumed: {units}")
print(f"Total Electricity Bill: INR {bill:.2f}")
