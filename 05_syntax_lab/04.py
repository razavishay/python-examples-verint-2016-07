"""
Read lines and print them
"""
lines = []
while True:
    line = raw_input()
    if line == "":
        break
    lines.append(line)
for i in range(0,len(lines)):
    print lines[len(lines)-1-i]
