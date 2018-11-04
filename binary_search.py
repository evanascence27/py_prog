#binary search
l1=list()
l=int(input("length of element list:"))
for i in range(l):
    l1.append((input("enter element:")))
print(l1)
x=input("enter element to search:")
start=0;end=l-1;mid=(start+end)//2
l1.sort()
while start<=end and end>=start:
    mid=(start+end)//2
    val=l1[mid]
    if val==x:
        print("element found")
        break
    elif x>val:
        start=mid+1
    else:
        end=mid-1
else:
    print("element not found")
