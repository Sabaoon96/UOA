"""
This program is used to test the three part 2 functions.
Complete the three functions.
The expected output is shown in the comment at the bottom of this file.
Author: Adriana Ferraro
"""

#----------------------------------------------------------
# Main function - Testing Part 2 of assignment 2
#----------------------------------------------------------
def main():
	print("get_how_many_match()")
	num_matches1 = get_how_many_match(2, [5, 2, 2, 5, 2]) 
	num_matches2 = get_how_many_match(5, [5, 2, 2, 5, 2]) 
	num_matches3 = get_how_many_match(4, [5, 2, 2, 5, 2]) 
	num_matches4 = get_how_many_match(3, [5, 3, 4, 3, 3]) 
	num_matches5 = get_how_many_match(6, [5, 2, 2, 6, 2]) 
	print(num_matches1, num_matches2, num_matches3, num_matches4, num_matches5)
	print("---------------------------")
	print("---------------------------")
	print("get_dice_number_with_two_matches()")
	two_matches1 = get_dice_number_with_two_matches([4, 5, 6, 5, 2]) 
	two_matches2 = get_dice_number_with_two_matches([4, 5, 3, 4, 2]) 
	two_matches3 = get_dice_number_with_two_matches([3, 3, 5, 4, 2])  
	two_matches4 = get_dice_number_with_two_matches([4, 5, 3, 2, 2]) 
	two_matches5 = get_dice_number_with_two_matches([4, 6, 6, 4, 2]) 
	print(two_matches1, two_matches2, two_matches3, two_matches4, two_matches5)
	print("---------------------------")
	print("---------------------------")
	print("get_max_number_of_matches()")
	max_matches1 = get_max_number_of_matches([4, 5, 6, 5, 2]) 
	max_matches2 = get_max_number_of_matches([4, 5, 3, 4, 2]) 
	max_matches3 = get_max_number_of_matches([3, 1, 2, 4, 5])  
	max_matches4 = get_max_number_of_matches([4, 5, 6, 5, 2]) 
	max_matches5 = get_max_number_of_matches([4, 5, 2, 5, 5]) 
	print(max_matches1, max_matches2, max_matches3, max_matches4, max_matches5)
	print("---------------------------")
	print("---------------------------")

#----------------------------------------------------------
# Functions which obtain the maximum number of matches and
# the dice number if there are exactly two matches
# Complete the following 3 functions below.
#----------------------------------------------------------
def get_how_many_match(value_to_match, list_of_dice):
	values = 0
	for dice in list_of_dice:
		if dice == value_to_match:
			values += 1
	return values
		
def get_dice_number_with_two_matches(list_of_dice):
	for dice in list_of_dice:
		matched = get_how_many_match(dice, list_of_dice)
		if matched == 2:
			return dice
		
def get_max_number_of_matches(list_of_dice):
	number_of_times_1 = 0
	number_of_times_2 = 0
	number_of_times_3 = 0
	number_of_times_4 = 0
	number_of_times_5 = 0
	number_of_times_6 = 0
	for dice in list_of_dice:
		if dice == 1:
			number_of_times_1 += 1
		elif dice == 2:
			number_of_times_2 += 1
		elif dice == 3:
			number_of_times_3 += 1
		elif dice == 4:
			number_of_times_4 += 1
		elif dice == 5:
			number_of_times_5 += 1
		elif dice == 6:
			number_of_times_6 += 1
	return max(number_of_times_1, number_of_times_2, number_of_times_3, number_of_times_4, number_of_times_5, number_of_times_6)
main()

"""
EXPECTED OUTPUT FOR PART 2
get_how_many_match()
3 2 0 3 1
---------------------------
---------------------------
get_dice_number_with_two_matches()
5 4 3 2 4
---------------------------
---------------------------
get_max_number_of_matches()
2 2 1 2 3
---------------------------
---------------------------
"""

