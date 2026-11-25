# Question 28: Write a program to check whether a character is a vowel or consonant.

char = 'e'

if char.isalpha() and len(char) == 1:
    if char.lower() in 'aeiou':
        print(f"'{char}' is a Vowel.")
    else:
        print(f"'{char}' is a Consonant.")
else:
    print("Invalid character input.")
