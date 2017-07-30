"""
Author:
Date-written: August 2015
Lab 5 Exercise 5.3
Finds the biggest word in a list of words
"""

def main():
	words_list = ["pig", "country", "short", "bye", "shorthand", "cat", "elephant", "at", "bye", "hello" ]
	biggest_word = get_biggest_word(words_list)
	print('"' + biggest_word + '"' + " is the biggest word in the list.")
	
def get_biggest_word(words_list):
	#You complete this function then delete this comment
	biggest_word = words_list[0]
	for word in words_list:
		if word > biggest_word:
			biggest_word = word
	return biggest_word		
main()