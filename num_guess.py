# Author: Angel Le
# GitHub username: lexuanangel
# Date: 1/25/2023
# Description: Number guessing game to get target integer

# set the correct guess to be the integer inputted
player_guess = 0
correct_guess = int(input("Enter the integer to for the player to guess.\n"))
print("Enter your guess.")
number_guess = 0

# create while loop to make sure the integer is correct
while player_guess != correct_guess:
    player_guess = int(input())
    if player_guess < correct_guess:
        print("Too low - try again: ")
    if player_guess > correct_guess:
        print("Too high - try again: ")
    number_guess += 1

# check number of guess with if else statement
if number_guess == 1:
    print("You guessed it in 1 try.")
else:
    print("You guessed it in " + str(number_guess) + " tries.")
