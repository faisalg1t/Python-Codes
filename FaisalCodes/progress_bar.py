"""
Code Name : Better Progress bar
Author : Shah Faisal
GitHub : @faisalg1t
"""

from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.03)

print("Done! 🎉")
