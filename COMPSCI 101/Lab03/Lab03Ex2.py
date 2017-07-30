"""
Lab 3 Ex 2
Author: Sabaoon Raza Khan

"""

def main():
	anns_bmi = calculate_bmi(63.2, 1.64)
	print_bmi("Ann", anns_bmi)
	
	bretts_bmi = calculate_bmi(79.2, 1.75)
	print_bmi("Brett", bretts_bmi)
	
	johns_bmi = calculate_bmi(85.5, 2.2)
	print_bmi("John", johns_bmi)

def calculate_bmi(weight, height):
	bmi = round(weight / (height * height), 1)
	return bmi

def print_bmi(name_of_person, bmi):
	print(name_of_person + "'s bmi is: " + str(bmi) + ".")
	
main()

