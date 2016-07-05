"""
receive 10 numbers and print the largest of them
"""
max = int(raw_input())
for i in range (9):
    b = int(raw_input())
    if b > max:
        max = b
print "Largest number is:", max
