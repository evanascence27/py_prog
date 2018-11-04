#table and break and continue
num=int(input("Enter number:"))
for i in range(1,11):
    if i==3 or i==6 or i==9:
        continue
    print("%d*%d=%d"%(num,i,num*i))
    if i==7:
        break
        
