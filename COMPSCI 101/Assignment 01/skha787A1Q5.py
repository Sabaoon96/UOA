"""
Sabaoon Raza Khan - skha787
ID Number: 983957824

Program used to create word chains.
"""

word = "frank"

print("Starting word: " + word)

position_prompt1 = int(input("Position: "))
replacement_letters_prompt1 = input("Replacement letters: ")
before_replacement_letters1 = word[0 : position_prompt1] #Letters of word before replacement letters.
after_replacement_letters1 = word[position_prompt1 + 2 :] #Letters of word after replacement letters.
word1 = before_replacement_letters1 + replacement_letters_prompt1 + after_replacement_letters1
print("1 Word is now: " + word1)

position_prompt2 = int(input("Position: "))
replacement_letters_prompt2 = input("Replacement letters: ")
before_replacement_letters2 = word1[0 : position_prompt2]
after_replacement_letters2 = word1[position_prompt2 + 2 :]
word2 = before_replacement_letters2 + replacement_letters_prompt2 + after_replacement_letters2
print("2 Word is now: " + word2)

position_prompt3 = int(input("Position: "))
replacement_letters_prompt3 = input("Replacement letters: ")
before_replacement_letters3 = word2[0 : position_prompt3]
after_replacement_letters3 = word2[position_prompt3 + 2 :]
word3 = before_replacement_letters3 + replacement_letters_prompt3 + after_replacement_letters3
print("3 Word is now: " + word3)

position_prompt4 = int(input("Position: "))
replacement_letters_prompt4 = input("Replacement letters: ")
before_replacement_letters4 = word3[0 : position_prompt4]
after_replacement_letters4 = word3[position_prompt4 + 2 :]
word4 = before_replacement_letters4 + replacement_letters_prompt4 + after_replacement_letters4
print("4 Word is now: " + word4)

equals_length = len(word) * 5 + len("->") * 5
print("=" * equals_length)
print(word + "->" + word1 + "->" + word2 + "->" + word3 + "->" + word4 + "->")
print("=" * equals_length)
