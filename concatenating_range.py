#concatenating given range
l1=list()
l2=list()
l=int(input("length of element list:"))
for i in range(l):
    l1.append((input("enter element:")))
print(l1)
n=int(input("value of n:"))
c=1
while c<=n:
    i=0
    while i<l:
        l2.append(l1[i]+str(c))
        i+=1
    c+=1
print(l2)
