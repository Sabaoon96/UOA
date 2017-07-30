"""
Lab 6 Ex 3
Author:
This program reads in a file of proverbs and
creates a new file by removing all the vowels.
"""
def main():
	proverbs = read_proverbs("Proverbs.txt")
	create_abbreviated_file(proverbs, "abbreviated-proverbs.txt")
	
def read_proverbs(filename):
	input_file = open(filename, "r")
	file_contents = input_file.read()
	input_file.close()
	return file_contents
	
def create_abbreviated_file(proverbs, filename):
	vowels = "AEIOUaeiou"
	output_file = open(filename, "w")
	non_vowels = ""
	for index in range(len(proverbs)):
		letter = proverbs[index]
		if vowels.find(letter) == -1:
			non_vowels += letter
	output_file.write(non_vowels)
	output_file.close()
	
main()

	

