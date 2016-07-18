class MyCounter(object):
    count = 0
    def __init__(self, count = 0):
        MyCounter.count += 1        

for _ in range(10):
    c1 = MyCounter()

# should print 10
print MyCounter.count
