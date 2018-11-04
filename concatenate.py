#conatenante ing/ily 
str=input("enter string:")
l=len(str)
if l>=3:
    if "ing" in str[l-3:]:
        print(str[:l-3]+'ly')
    else:
        print(str[:l-2]+'ing')
else:
    print(str)
