def SumNumbers (list):
    s = 0
    for i in list:
        if type(i) == int:
            s += i
    return s

def MultiplyNumbers (list):
    m=1
    for i in list:
        if type(i) == int:
            m *= i
    return m

