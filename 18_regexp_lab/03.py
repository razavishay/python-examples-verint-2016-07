import re
import sys

filename = sys.argv[1]

with open (filename, 'r') as f:
    for line in f:
        sys.stdout.write(re.sub(r'(\w+),(\w+),(.*)', lambda m: m.group(2)+ ',' + m.group(1)+ ',' + m.group(3), line))
        
