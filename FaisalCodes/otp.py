"""
Code Name : OTP Example
Author : Shah Faisal
GitHub : @faisalg1t
"""

import random

otp = random.randint(1000, 9999)

print("Your OTP is:", otp)

user = int(input("Enter OTP: "))

if user == otp:
    print("Verification successfull")

else:
    print("Inavlid OTP")
