"""
Sabaoon Raza Khan
skha787 - 983957824
This game of Dicey consists of 3 rounds, with two players getting a turn each at rolling the dice in every round. The player with the highest score at the end, wins.
"""

import random

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

def main():
	round_number = 1
	player1_total_score = 0
	player2_total_score = 0
	player1_name = "Sabaoon"
	player2_name = "Abbaas"
	display_welcome()
	player1_total_score = process_player_turn(player1_name)
	player2_total_score = process_player_turn(player2_name)
	results_round1 = display_round_results(round_number, player1_name, player1_total_score, player2_name, player2_total_score)
	player1_total_score += process_player_turn(player1_name)
	player2_total_score += process_player_turn(player2_name)
	results_round2 = display_round_results(round_number + 1, player1_name, player1_total_score, player2_name, player2_total_score)
	player1_total_score += process_player_turn(player1_name)
	player2_total_score += process_player_turn(player2_name)
	results_round3 = display_round_results(round_number + 2, player1_name, player1_total_score, player2_name, player2_total_score)
	display_final_results(player1_name, player1_total_score, player2_name, player2_total_score)
main()