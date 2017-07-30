"""
Lab 3 Ex 1
Author: Sabaoon Raza Khan

"""

def main():
	ounces = get_ounces_from_user()
	grams = convert_ounces_to_grams(ounces)
	print_conversion(ounces, grams)
	
def get_ounces_from_user():
	ounces = int(input("Enter ounces: "))
	return ounces
	
def convert_ounces_to_grams(ounces):
	grams = round(ounces * 28.3495231)
	return grams

def print_conversion(ounces, grams):
	print(str(ounces) + " ounces is equivalent to " + str(grams) + " grams.")
	
main()

