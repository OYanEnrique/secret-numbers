#Secret Number Game

from random import randint

guess = 0
player_guess = -1
secret_number = randint(1,10)

while player_guess != secret_number:
	player_guess = int(input('Try to guess a number between 1 and 10:\n'))
	guess += 1
	if player_guess != secret_number:
		print('Try again!')
	
print(f'Congratulations you guessed the number {secret_number}, it took {guess} tries!')