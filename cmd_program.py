from sys import *
from argparse import *


n = len(argv)
args = argv
print("the number are:",args[1:])
print("sum of two numbers are:",int(args[1])+int(args[2]))


parser = ArgumentParser(description="This program is about adding numbers")
parser.add_argument("n1",type=int,help="please enter the number")
parser.add_argument("n2",type=int,help="please enter the number")
args = parser.parse_args()
result=int(args.n1)+int(args.n2)
print("result:",result)



