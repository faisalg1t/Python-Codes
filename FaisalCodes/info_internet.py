"""
Code Name : Get Info from internet
Author : Shah Faisal
GitHub : @faisalg1t
"""

import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status:", response.status_code)
print(response.json())
