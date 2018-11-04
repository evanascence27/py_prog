str=input("enter string:")
for i in range(len(str)):
    if str[i] not in str[:i]:
        print("%c occurs %d times"%(str[i],str.count(str[i])))
