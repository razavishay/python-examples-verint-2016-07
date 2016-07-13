import sys
names=sys.argv[1:]
print "names=", names
hostsFile = "C:\\Python Course\\2\\hosts.txt"
hostsDict = {}
with open(hostsFile, 'r') as f:
    for line in f:
        ipAddr=line.split('=')[1]
        hostname=(line.split('=')[0]).strip()
        hostsDict.setdefault(hostname,0)
        hostsDict[hostname]=ipAddr.strip()

print hostsDict
for n in names:
    if n in hostsDict:
        print "IP of %s is %s" % (n, hostsDict[n])
    else:
        print "%s is not on the list!" %n

