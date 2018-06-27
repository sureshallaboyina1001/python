import logging 

logging.basicConfig(filename='log.txt', level=logging.ERROR)
try:
    a,b=[int(x)for x in input("enter two numbers:").split(',')]
    c=a/b
except EXception as e:
    logging.exception(e)
else:
    print(c)
