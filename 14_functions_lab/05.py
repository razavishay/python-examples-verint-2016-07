def GroupBy(func, myList):
    myDict = {}
    for el in myList:
        theKey =  func(el)
        if myDict.get(theKey) == None:
            myDict[theKey] = [el]
        
        else:
            myDict[theKey].append(el)
    print
    return myDict
    
