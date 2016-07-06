import sys
try:
    float(sys.argv[1])
    float(sys.argv[2])
except:
    print "Input must consist of two whole numbers"
    sys.exit()
a = float(sys.argv[1])
b = float(sys.argv[2])
print "The sum of %f and %f is %f" %(a, b, a+b)
