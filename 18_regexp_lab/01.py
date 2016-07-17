import sys
import re

filename = sys.argv[1]
key = sys.argv[2]
with open(filename, 'r') as f:
    for line in f:
        r = re.search(r'^(\w+)\s*=\s*(\w+)', line)
        if r is not None and r.groups()[0] == key:
            print r.groups()[1]
            

