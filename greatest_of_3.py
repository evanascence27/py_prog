#greatest among 3
a=int(input("Enter no:"))
b=int(input("Enter no:"))
c=int(input("Enter no:"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
