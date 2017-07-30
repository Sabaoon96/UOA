"""
Lab 6 Ex 2
Author:
This program generates sentences made up of randomly selected words.
"""

import random

def main():
	adjectives_list = get_words_list("adjectives.txt")
	nouns_list = get_words_list("nouns.txt")
	adverbs_list = get_words_list("adverbs.txt")
	verbs_list = get_words_list("verbs.txt")
	sentence = create_sentence(adjectives_list, nouns_list, adverbs_list, verbs_list)
	print(sentence)

def get_words_list(filename):
	input_file = open(filename, "r")
	file_contents = input_file.read()
	input_file.close()
	list_of_words = file_contents.split()
	return list_of_words
	
def create_sentence(adjectives_list, nouns_list, adverbs_list, verbs_list):
	random_adjective = get_random_word(adjectives_list)
	random_noun = get_random_word(nouns_list)
	random_adjective1 = get_random_word(adjectives_list)
	random_noun1 = get_random_word(nouns_list)
	random_adverb = get_random_word(adverbs_list)
	random_verb = get_random_word(verbs_list)
	sentence = random_adjective + " " + random_noun + " " + random_adverb + " " + random_verb + " " + random_adjective1 + " " + random_noun1 + "."
	return sentence.capitalize()
	
def get_random_word(words_list):
	random_num = random.randrange(len(words_list))
	random_word = words_list[random_num]
	return random_word
	
main()
	
	

