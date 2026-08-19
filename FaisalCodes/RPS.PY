"""
Code Name : Rock Paper Scissors
Author : Shah Faisal
GitHub : @faisalg1t
"""

import random

choices = ["rock", "paper", "scissors"]

player = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    print("🤝 It's a tie!")
elif (
    (player == "rock" and computer == "scissors") or
    (player == "paper" and computer == "rock") or
    (player == "scissors" and computer == "paper")
):
    print("🏆 You win!")
else:
    print("💀 You lose!")
