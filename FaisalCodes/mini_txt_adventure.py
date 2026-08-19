"""
Code Name : Mini Text Adventure
Author : Shah Faisal
GitHub : @faisalg1t
"""

print("🏰 THE DARK CASTLE")
print("You are standing outside a mysterious castle.")

choice = input("Do you enter or run? ").lower()

if choice == "enter":
    print("\nYou enter the castle...")
    door = input("There are two doors. Choose left or right: ").lower()

    if door == "left":
        print("👑 You found the treasure! YOU WIN!")
    elif door == "right":
        print("👻 A ghost scares you! GAME OVER!")
    else:
        print("You stand there confused. 😂")
else:
    print("🏃 You ran away safely!")
