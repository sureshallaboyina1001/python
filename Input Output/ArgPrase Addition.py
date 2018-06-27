#Parsing Command Line Arguments
#Add to numbers

from argparse import *

parser = ArgumentParser(description="Adding two numbers")
parser.add_argument("num1",type=float,help="Please give the FLOAT type number")
parser.add_argument("num2",type=float,help="Please give the FLOAT type number")
args=parser.parse_args()
result=float(args.num1)+float(args.num2)
print("sum is :",result)
