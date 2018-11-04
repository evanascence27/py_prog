#removing duplicates
l1=list()
for i in range(5):
    l1.append((input("enter element:")))
print(l1)
i=0
while i<len(l1):
        j=i+1
        while j<len(l1):
            if l1[i]==l1[j]:
                del l1[j]
            else:
                j+=1
        i+=1
print(l1)

