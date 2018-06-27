#passing values from command prompt

from sys import *

n = len(argv)
args = argv
print('no of command line arguments: ',n )
for i in args:
    print(i)
