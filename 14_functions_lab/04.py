def longer_than(minLength, *list):
    refinedList = []
    for word in list:
        if len(word) > minLength:
            refinedList.append(word)
    return refinedList

print longer_than(3, 'abc', 'zzzzz', 'cba', 'bb', 'abcd')
