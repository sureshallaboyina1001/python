# ASSERT statement example

num = int(input("enter the number:"))
assert num>0 ,"wrong input"
print("U entered:",num)


try:
    num = int(input("enter the number:"))
    assert num>0
    print("U entered:",num)
except AssertionError:
    print("Wrong Input Entered")
