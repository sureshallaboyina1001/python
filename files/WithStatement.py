with open("sample.txt",'w')as f:
    f.write("This is with statement\n")
    f.write("python is attractive")
with open("sample.txt",'r')as fr:
    for line in fr:
        print(line)
