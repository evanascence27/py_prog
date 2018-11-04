#armstrong in range
c=0;i=10
while c<5:
    copy=i;add=0;n=0
    while copy>0:
        n+=1
        copy//=10
    copy=i
    while copy>0:
        d=copy%10
        add+=d**n
        copy//=10
    if add==i:
        c+=1
        print(i)
    i+=1
