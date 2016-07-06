"""
Logg for a number under 1000000 to divide with 7, 13 & 15
"""
from random import randint
while True:
    r = randint (1, 1000000)
    if r % 15 == 0 and r % 13 == 0 and r % 7 == 0:
        print r
        break
