"""
Lab 8 Ex 3
Author: Sabaoon Raza Khan
This program translates words into radio telephone language.
"""
def main():
	radio_telephone_alphabet = ('Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
		'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 
		'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu', ' ', ',', '?', '!', '.')
	radio_telephone_dictionary = create_radio_telephone_dict(radio_telephone_alphabet)
	word = get_word_from_user()
	display_translation(word, radio_telephone_dictionary)
	
def create_radio_telephone_dict(radio_telephone_alphabet):
	alphabet_dict = {}
	for element in radio_telephone_alphabet:
		key = element[0]
		alphabet_dict[key] = element
	return alphabet_dict
	
def get_word_from_user():
	word = input("Enter the word to be translated: ")
	return word
	
def display_translation(word, rt_dictionary):
	word_upper = word.upper()
	translation = ""
	for element in word_upper:
		if element in rt_dictionary:
			translation += rt_dictionary[element] + " "
	print(translation)
	
main()