"""
Lab 8 Ex 1
Author: Sabaoon Raza Khan
This program produces a letter count summary of the sentence entered by the user.
"""
def main():
	sentence = get_sentence_from_user()
	sentence = sentence.lower()
	letter_counts_dict = count_letter_occurrences(sentence)
	print(letter_counts_dict)
	
def get_sentence_from_user():
	sentence = input("Enter a sentence: ")
	return sentence

def count_letter_occurrences(sentence):
	count_dict = {}
	for letter in sentence:
		if letter.isalpha():
			letter = letter.lower()
			if letter not in count_dict:
				count_dict[letter] = 1
			else:
				count_dict[letter] += 1
	return count_dict
	
main()