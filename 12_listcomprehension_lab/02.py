abc=range(97,97+26)
#print abc
x = [chr(a)+chr(b)+chr(c) for a in abc for b in abc for c in abc]
print x
