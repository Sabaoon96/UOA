"""
Sabaoon Raza Khan - skha787
ID Number: 983957824

Program that encrypts and decrypts messages, 25 letters in length.
"""

original_message = "Pagg rm rfomieugisanrn t!"
#Makes sure the message is 25 letters in length
message = original_message * 25
message = message[0 : 25]

first_five_letters = message[0 : 5]
second_five_letters = message[5 : 10]
third_five_letters = message[10 : 15]
fourth_five_letters = message[15 : 20]
fifth_five_letters = message[20 : 25]

first_column = first_five_letters[0] + second_five_letters[0] + third_five_letters[0] + fourth_five_letters[0] + fifth_five_letters[0]
second_column = first_five_letters[1] + second_five_letters[1] + third_five_letters[1] + fourth_five_letters[1] + fifth_five_letters[1]
third_column = first_five_letters[2] + second_five_letters[2] + third_five_letters[2] + fourth_five_letters[2] + fifth_five_letters[2]
fourth_column = first_five_letters[3] + second_five_letters[3] + third_five_letters[3] + fourth_five_letters[3] + fifth_five_letters[3]
fifth_column = first_five_letters[4] + second_five_letters[4] + third_five_letters[4] + fourth_five_letters[4] + fifth_five_letters[4]

print("Original message: " + original_message)
print("Encrypted message: " + first_column + second_column + third_column + fourth_column + fifth_column)

