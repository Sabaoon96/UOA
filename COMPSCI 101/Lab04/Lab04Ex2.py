"""
Lab 04 Exercise 4.2
Plays the "guess my number" game
"""
import random

def main():
	play_guessing_game()
	
def play_guessing_game():
	# You complete this function according to the psuedocode provided.
	target_number = random.randrange(1, 101)
	guess = 0
	
	guess = int(input("Guess a number between 1 and 100: "))
	
	while guess != target_number:
		if guess > target_number:
			print(guess, "is too high.")
			
		elif guess < target_number:
			print(guess, "is too low.")
			
		guess = int(input("Guess a number between 1 and 100: "))
		
	print("Yes. Well done!!")
				
def get_guess_from_user():
	guess = int(input("Guess a number between 1 and 100: "))
	return guess
	
main()
	