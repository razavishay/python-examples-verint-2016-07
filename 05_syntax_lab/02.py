from random import randint
sum = 0
for i in range(7):
    x = randint(1,100)
    sum += x
print "Sum is ", sum
if sum % 7 == 0:
    print "BOOM"
