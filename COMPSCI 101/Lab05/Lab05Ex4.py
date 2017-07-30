"""
Author:
Date-written: August 2015
Lab 5 Exercise 5.4
Outputs a list of words that contain a particular letter.
"""

def main():
	selected_words = get_selected_words("a", "The road was long and winding")
	print("List of words containing a:", selected_words)
	selected_words = get_selected_words("e", "The quick brown fox jumps over the lazy dog")
	print("List of words containing e:", selected_words)
	
def get_selected_words(letter, sentence):
	# You complete this function then delete this comment
	sentence = sentence.lower()
	words_list = sentence.split()
	return_list = []
	for word in words_list:
		if word not in return_list and letter in word:
			return_list += [word]
	return return_list

main()