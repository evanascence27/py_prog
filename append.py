#append list to second list
l1=list()
l2=list()
for i in range(5):
    l1.append((input("enter element:")))
for i in range(5):
    l2.append((input("enter element:")))
print(l1)
print(l2)
for i in range(5):
    l1.append(l2[i])
print(l1)
