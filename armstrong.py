#armstrong
n=int(input("eneter no:"))
copy=n;add=0
while copy>0:
    d=copy%10
    add+=d**3
    copy//=10
if add==n:
    print("Armstrong")
else:
    print("not")
