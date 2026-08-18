"""
Code Name : Number Guessing Game
Author : Shah Faisal
GitHub : @faisalg1t
"""

import random

number = random.randint(1, 100)
attempts = 0

print("🎯 I'm thinking of a number from 1 to 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < number:
        print("⬆️ Too low!")
    elif guess > number:
        print("⬇️ Too high!")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
