for i in range(1,8,2):
    for j in range(7,i,-2):
        print(" ",end='')
    for j in range(1,i+1):
        print("*",end='')
    print()
for i in range(5,0,-2):
    for j in range(5,i-1,-2):
        print(" ",end='')
    for j in range(1,i+1):
        print("*",end='')
    print()
