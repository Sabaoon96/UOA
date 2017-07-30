"""
Author:
Date-written: August 2015
Lab 5 Exercise 5.5
Rounds a list of numbers to whole numbers.
"""

def main():
	numbers = [7.5, 8.5, 7.3, 3.7, 4.21, 5.25, 49.18]
	print("Original list of numbers:", numbers)
	round_to_whole_numbers(numbers)
	print("List of numbers is now:  ", numbers)
	
def round_to_whole_numbers(numbers_list):
	# You complete this function then delete this comment
	for index in range(0, len(numbers_list)):
		numbers_list[index] = round(numbers_list[index])
main()