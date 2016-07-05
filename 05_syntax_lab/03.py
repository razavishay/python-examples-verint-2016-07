"""
Take a number from 1 to 10000 and print the sum of its digits
"""
from random import randint
x = str(randint(1,10000))
print "Number is", x
sum = 0
for i in range (len(x)):
    sum += int(x[i])
print "Sum of digits is", sum
