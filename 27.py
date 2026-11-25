# Question 27: Write a program to assign grades based on student marks using if-elif-else.

marks = 82.5

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print(f"Marks: {marks}")
print(f"Assigned Grade: {grade}")
