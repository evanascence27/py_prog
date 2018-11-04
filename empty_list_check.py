#convert list of chars to string
l1=list()
for i in range(5):
    l1.append((input("enter element:")))
print(l1)
s=l1[0]
for i in range(1,5):
    s+=l1[i]
print(s)
