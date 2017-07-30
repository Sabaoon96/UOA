"""
Lab 8 Ex 2
Author: Sabaoon Raza Khan
This program reads in a file of palindromes and produces a summary of the word lengths of the palindromes.
"""
def main():
	palindromes_list = get_palindromes_list("palindromes.txt")
	word_length_dictionary = create_word_length_dictionary(palindromes_list)
	display_summary(word_length_dictionary)
	
def get_palindromes_list(filename):
	input_file = open(filename, "r")
	file_contents = input_file.read()
	input_file.close()
	list_of_words = file_contents.split()
	return list_of_words
	
def create_word_length_dictionary(palindromes_list):
	palindromes_dict = {}
	for word in palindromes_list:
		if len(word) not in palindromes_dict:
			palindromes_dict[len(word)] = word + " "
		else:
			palindromes_dict[len(word)] += word + " "
	return palindromes_dict
	
			
def display_summary(word_length_dictionary):
	print("Palindromes Summary")
	print("=" * len("Palindromes Summary"))
	for length, words in word_length_dictionary.items():
		print("Word length of ", length, ":", sep = "")
		print(words)
		print()
main()