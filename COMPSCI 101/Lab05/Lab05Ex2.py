"""
Author:
Date-written: August 2015
Lab 5 Exercise 5.2
Outputs words which are less than 4 letters long
"""

def main():
	words_list = ["piano", "hat", "hello", "egg", "good", "he", "aeroplane", "a", "the"]
	short_letter_words_list = create_short_letter_words_list(words_list)
	print(short_letter_words_list)
	
def create_short_letter_words_list(words_list):
	#You complete this function then delete this comment
	words_less_than_4 = []
	for words in words_list:
		if len(words) < 4:
			words_less_than_4 += [words]
	return words_less_than_4		
main()