"""
Code Name : Random Password Generator
Author : Shah Faisal
GitHub : @faisalg1t
"""

import random
import string

length = int(input("Password length: "))

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = ""

for i in range(length):
    password += random.choice(characters)

print("🔐 Your password:", password)
