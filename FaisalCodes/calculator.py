"""
PythonCode : 004
Code Name : Calculator
Author : Shah Faisal
GitHub : @faisalg1t
"""

num1 = int(input("Number: "))
opr = input("Opr +, -, *, /: ")
num2 = int(input("Number: "))

if opr == "+":
    result = num1 + num2

elif opr == "-":
    result = num1 - num2

elif opr == "*":
    result = num1 * num2

elif opr == "/":
    result = num1 / num2

else:
    result = "You are nigga"

print(num1, opr, num2, "=", result)
