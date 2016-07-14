def checktypes (num, string):
    if type(num) <> int:
        raise Exception ("First argument must be int")
    elif type(string) <> str:
        raise Exception ("Second argument must be string")
    else:
        print "Argument check passed."
