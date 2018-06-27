from argparse import *

parser = ArgumentParser(description="This is the Program for square values ")
parser.add_argument("num",type=int,help="Please input the Integer type number")
args=parser.parse_args()
result=args.num**2
print("Square is:",result)
