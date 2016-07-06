import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Get Path and file sizes according to user input')
parser.add_argument('-p', nargs = 1, default = '.', help = 'The Path where files are to be searched', metavar = 'PATH')
parser.add_argument('-s', nargs = 1, default = 1, type = int, help = "Minimum file size (MB) to look for", metavar = "SIZE")
args = parser.parse_args()
path = args.p[0]
sizeToSearchMega = args.s[0]
sizeToSearchBytes = 1024 * 1024 * sizeToSearchMega
for root, dirs, files in os.walk(path):
    for filename in files:
        file_path = os.path.join(root,filename)
        statInfo = os.stat(file_path)
        if statInfo.st_size > sizeToSearchBytes:
            print "%s is %d MB" %(file_path, statInfo.st_size / 1024 / 1024)
