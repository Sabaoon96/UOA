"""
Lab 6 Ex 1
Author:
This program creates a file of palindromes.
"""

def main():
	words_list = get_words_list("words.txt")
	create_file_of_palindromes(words_list, "palindromes.txt")

def get_words_list(filename):
	input_file = open(filename, "r")
	file_contents = input_file.read()
	input_file.close()
	list_of_words = file_contents.split()
	return list_of_words

def create_file_of_palindromes(words_list, output_filename):
	output_file = open(output_filename, "w")
	for word in words_list:
		if word == word[ : : -1]:
			output_file.write(word + "\n")
	output_file.close()
	
main()
	
	

