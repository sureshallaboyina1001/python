with open("x.txt",'w') as f:
    while str !='@':
        str=input()
        if str !='@':
            f.write(str+"\n")
  
    f.close()