#sum and multiplication of elements in a list
l1=list()
s=0;m=1
for i in range(5):
    l1.append(int(input("enter number:")))
    s+=l1[i]
    m*=l1[i]
print(l1)
print("sum={} and product={}".format(s,m))

