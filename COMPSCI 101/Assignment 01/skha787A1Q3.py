"""
Sabaoon Raza Khan - skha787
ID Number: 983957824

Program which prints a 5 letter word in the form of a parallelogram.
"""

word = "CATHY"

blanks = " "
#Indicates the number of blanks there should be before the word.
row1 = blanks * int(5) 
row2 = blanks * int(4)
row3 = blanks * int(3)
row4 = blanks * int(2)
row5 = blanks * int(1)

print("*" * 9)
print("*" * 9)
print(row1, word[0])
print(row2, word[1:3])
print(row3, word[1:4])
print(row4, word[1:5])
print(row5, word[:6])
print(row5, word[1:])
print(row5, word[2:])
print(row5, word[3:])
print(row5, word[4])
print("*" * 9)
print("*" * 9)