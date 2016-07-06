"""
get least common multiple of two numbers between 1 and 10
"""
from random import randint
a = randint (1, 10)
b = randint (1, 10)
i = 0
while True:
    i += 1
    if i % a == 0 and i % b == 0:
        print "First number: %d, Second number: %d, LCM: %d" % (a, b, i)
        break
    # Safety measure
    if i > a * b:
        break
