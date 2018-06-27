with open("line.txt","r+b") as f:
    f.write(b'Amazing Python')
    f.seek(5)
    print(f.read(2))
    print(f.tell())
f.close()
