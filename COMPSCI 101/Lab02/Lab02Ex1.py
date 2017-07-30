"""
COMPSCI101 Lab-02
Author: Sabaoon Raza Khan
"""

# Exercise 2.1:
print()
print("You will be asked to provide your full name.")
print("A middle name is a must.")
print()

input("Press 'Enter' to continue")
print()

user_full_name =  input("Enter your full name: ")
full_name = user_full_name.strip()

space1_position = full_name.find(" ")
first_name = full_name[0 : space1_position]

space2_position = full_name.rfind(" ")
last_name = full_name[space2_position + 1: ]

middle_name = full_name[space1_position + 1 : space2_position + 1]
middle_name = middle_name.strip()

first_initial = first_name[0]
middle_initial = middle_name[0]
last_initial = last_name[0]

user_initials = first_initial + middle_initial + last_initial
user_initials = user_initials.upper()

print(user_initials)
print(last_name + "," , first_name, middle_name)








