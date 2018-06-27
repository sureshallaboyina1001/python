str="Dear Suresh"
with open("data.bin",'wb') as f:
    f.write(str.encode())
    f.write(b"hello")
    print(str.decode())
