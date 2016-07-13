import sys
from collections import Counter
print "Please give me a file"
wordsFile=raw_input()
words=[]
counterList=[]
dict={}
with open(wordsFile, 'r') as f:
    for line in f:
        word=line.strip()
        words.append(word)
        cnt=Counter(word)
        if cnt not in counterList:
            counterList.append(cnt) 

for cnt in counterList:
    for word in words:
        if Counter(word)==cnt:
            print word, " ",
    print


            
        
        
        
