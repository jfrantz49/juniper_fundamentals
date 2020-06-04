"""
The Game of Dice
--------------

Another command line game in python
We'll make use of data structures

Game play: To simulate the flipping coin
To have the program to randomly select a side of the coin
Give the user the ability to guess the side of the coin landed on
If the user guess the correct side then they win
If they guessed the incorrect side then they'll lose
The user can play the game an infinite amount of times
When the user types 'done' then the program exits
Then, the program will return how many games the user won,
and how many they lost
"""

import random

correct, wrong = 0, 0

while True:
    side = random.choice(['heads', 'tails'])
    user_input = input("Type 'heads' or 'tails' or 'done ")
    if user_input == 'done':
        print("Game Over...")
        print('Number of correct guesses ', correct)
        print('Number of incorrect guesses ', wrong)
        break
    elif user_input == side:
        print("You Win!")
        correct += 1
    else:
        print("Try again")
        wrong += 1