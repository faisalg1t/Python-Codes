"""
PythonCode : 001
Code Name : Number Guessing Game
Author : Shah Faisal
GitHub : @faisalg1t
"""

import random

number = random.randint(1, 100)

print("Guess the Number!")
print("I'm thinking of a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print(" To low! Try again.")
    elif guess > number:
        print("To high! Try again.")
    else:
        print("Correct! you guessed the number!")
        break