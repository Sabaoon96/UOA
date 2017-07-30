"""
This program is used to test the three part 3 functions.
Complete the three functions.
The expected output is shown in the comment at the bottom of this file.

*** MAKE SURE YOU COPY YOUR PART 1 AND PART 2 FUNCTIONS INTO THIS PROGRAM ***
Author: Adriana Ferraro
"""

import random

#----------------------------------------------------------
# Main function - Testing Part 3 of assignment 2
#----------------------------------------------------------
def main():
	print("get_list_of_dice_rolls()")
	print("Note:  the dice values are random so your output will be different.")
	print()
	dice_rolls1 = get_list_of_dice_rolls(3) 
	dice_rolls2 = get_list_of_dice_rolls(1) 
	dice_rolls3 = get_list_of_dice_rolls(5) 
	dice_rolls4 = get_list_of_dice_rolls(4) 
	print("Should be a list of 3 random dice values:", dice_rolls1)
	print("Should be a list of 1 random dice value:", dice_rolls2)
	print("Should be a list of 5 random dice values:", dice_rolls3)
	print("Should be a list of 4 random dice values:", dice_rolls4)
	print("---------------------------")
	print("---------------------------")
	print("get_score()")
	score1 = get_score([4, 6, 6, 6, 6]) 
	score2 = get_score([4, 5, 6, 5, 6]) 
	score3 = get_score([6, 6, 2, 2, 2]) 
	score4 = get_score([5, 5, 6, 5, 5]) 
	score5 = get_score([6, 6, 6, 6, 6]) 
	score6 = get_score([6, 5, 1, 3, 2]) 
	print(score1, score2, score3, score4, score5, score6)
	print("---------------------------")
	print("---------------------------")
	print("Note:  the dice values are random so your output will be different.")
	print("Check that the scores are correct for the dice which are rolled.")
	print()
	print("process_player_turn()")
	player_score1 = process_player_turn("Adriana")
	print("Player score: ", player_score1)
	print()
	player_score2 = process_player_turn("Joe")
	print("Player score: ", player_score2)
	print("---------------------------")
	print("---------------------------")
#----------------------------------------------------------
# Functions which process a player's turn.
# Complete the following 3 functions below.
#----------------------------------------------------------
def get_list_of_dice_rolls(number_of_rolls):
    return [random.randrange(1, 7) for i in range(number_of_rolls)]
 
def get_score(list_of_dice):
	matches = get_max_number_of_matches(list_of_dice)
	score = 0
	if matches == 1 or matches == 2:
		score = 0
	elif matches == 3:
		score = 3
	elif matches == 4:
		score = 4
	elif matches == 5:
		score = 5
	return score
	
def process_player_turn(player_name):
	player_turn = display_turn_info(player_name)
	five_random_dice_rolls = get_list_of_dice_rolls(5)
	dice_list = display_dice(five_random_dice_rolls)
	max_matches = get_max_number_of_matches(five_random_dice_rolls)
	if max_matches == 2:
		dice_value = get_dice_number_with_two_matches(five_random_dice_rolls)
		elements_list = [dice_value, dice_value]
		two_matches = display_exactly_two_matches_message(dice_value)
		three_random_dice_rolls = get_list_of_dice_rolls(3)
		elements_list += (three_random_dice_rolls)
		new_dice_list = display_dice(elements_list)
		final_score = get_score(elements_list)
		return final_score
	else:
		return get_score(five_random_dice_rolls)
	
#----------------------------------------------------------
# Functions from part 2
# which obtain the maximum number of matches and
# the dice number if there are exactly two matches
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
	
#----------------------------------------------------------
# Functions from part 1
#----------------------------------------------------------	
def display_welcome():
	print()
	print("Welcome to DICEY, written by skha787")
	print()
	
def display_turn_info(player_name):
	print("  " + player_name + "'s turn")
	
def display_dice(list_of_dice):
	print("    Dice:  ", end = "")
	for numbers in list_of_dice:
		print(numbers, end = " ")
	print()
	
def display_exactly_two_matches_message(dice_number):
	print("    Two ", dice_number, "'s. Roll the remaining 3 dice.", sep = "")
	
def display_round_results(round_number, player1_name, player1_score, player2_name, player2_score):
	print("Round ", round_number, " results: ", player1_name, " has ", player1_score, " points, and ", player2_name, " has ", player2_score, " points", sep = "")
	print()

def display_final_results(player1_name, player1_score, player2_name, player2_score):
	print()
	if player1_score > player2_score:
		message = "Congratulations to " + player1_name
		print("*" * len(message))
		print(message)
		print("*" * len(message))
	elif player2_score > player1_score:
		message = "Congratulations to " + player2_name
		print("*" * len(message))
		print(message)
		print("*" * len(message))
	elif player1_score == player2_score:
		message = "The result is a tie"
		print("*" * len(message))
		print(message)
		print("*" * len(message))
	print()	
	
main()

"""
EXPECTED OUTPUT FOR PART 3
get_list_of_dice_rolls()
Note:  the dice values are random so your output will be different.

Should be a list of 3 random dice values: [6, 4, 2]
Should be a list of 1 random dice value: [6]
Should be a list of 5 random dice values: [1, 4, 3, 5, 3]
Should be a list of 4 random dice values: [2, 1, 3, 3]
---------------------------
---------------------------
get_score()
4 0 3 4 5 0
---------------------------
---------------------------
Note:  the dice values are random so your output will be different.
Check that your scores are correct for the dice which are rolled.

process_player_turn()
  Adriana's turn
    Dice:  6 2 3 4 5
Player score:  0

  Joe's turn
    Dice:  5 2 6 1 2
    Two 2's. Roll the remaining 3 dice.
    Dice:  2 2 6 4 6
Player score:  0
---------------------------
---------------------------
"""

