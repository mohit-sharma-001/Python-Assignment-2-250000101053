# Question 19: Write a program to demonstrate identity operators is and is not.

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 =", list1)
print("list2 =", list2)
print("list3 is reference to list1")

print("list1 == list2 :", list1 == list2, "(Values are equal)")
print("list1 is list2 :", list1 is list2, "(Different memory objects)")
print("list1 is list3 :", list1 is list3, "(Same memory object)")
print("list1 is not list2:", list1 is not list2)
