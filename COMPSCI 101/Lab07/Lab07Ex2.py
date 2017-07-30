"""
Lab 7 Ex 2
Author: Sabaoon Raza Khan
Date: September, 2015
This program generates and prints all the anagrams
of the word entered by the user.

"""
def main():
	words_list = get_words_list("words.txt")
	word = get_word_from_user()
	anagrams_tuple = get_anagrams(word, words_list)
	print(anagrams_tuple)
	
def get_words_list(filename):
	input_file = open(filename, "r")
	file_contents = input_file.read()
	input_file.close()
	list_of_words = file_contents.split()
	return list_of_words
	
def get_word_from_user():
	word = input("Enter a word: ")
	return word
	
def convert_to_sorted_letters(word):
	letters = list(word)
	letters.sort()
	return letters

def get_anagrams(user_word, words_list):
	user_sorted_list = convert_to_sorted_letters(user_word)
	anagrams = []
	for word in words_list:
		sorted_word = convert_to_sorted_letters(word)
		if sorted_word == user_sorted_list:
			anagrams.append(word)
	return tuple(anagrams)
	
	
main()    



