def TensSum(*list):
    s = 0
    for number in list:
        if type(number) == int:
            numberAsString = str(number)
            if len(numberAsString) < 2:
                s += 0
            else:
                s += int(numberAsString[-2:-1])
    return s



print TensSum (10,20,360,1,60)
