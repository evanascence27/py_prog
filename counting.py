#counting
l1=list()
c=0
for i in range(5):
    l1.append((input("enter string:")))
    if len(l1[i])>=2 and l1[i][0]==l1[i][-1]:
        c+=1
print(l1)
print("count=%d"%(c))

