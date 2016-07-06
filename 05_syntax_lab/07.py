from random import randint
numberToGuess = randint (1,100)
mistakeChance = 0.2 # 20% change of prompting wrong message to the user
print "Please choose a number between 1 to 100:"
while True:
    userGuess = int(raw_input())
    wrongAnswerChance = randint (0,100) # can be also outside the while loop to have it constant throgh the run
    if userGuess >= 0 and userGuess <= 100:
        if userGuess == numberToGuess: # right guess
            if wrongAnswerChance > 100 * mistakeChance: # print the right answer
                print "This is right! %d is the number" % userGuess
                break
            else: # give him a wrong answer
                print "Wrong guess, try again"
        else: # wrong guess
             if wrongAnswerChance > 100 * mistakeChance: # print the right answer
                 print "Wrong guess, try again"
             else: # do nothing... we don't tell him he's right if he's wrong
                 print "Wrong guess, try again"
    elif userGuess > 100:
        print "%d is greater than 100. Try again." % userGuess
    else:
        print "%d is lesser than 1. Try again" %userGuess

