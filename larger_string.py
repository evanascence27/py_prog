#anagram
'''str1=input("enter string 1:")
str2=input("enter string 2:")
if len(str1)>len(str2):
    print(str1)
elif len(str1)==len(str2):
    for i in range(len(str1)):
        if ord(str1[i])>ord(str2[i]):
            print(str1)
            break
        else:
            print(str2)
            break
else:
    print(str2)'''
str1=input("enter string 1:")
str2=input("enter string 2:")
if (str1)>(str2):
    print(str1)
elif (str1)==(str2):
    print("EQUAL")
else:
    print(str2)
    
str1=str2
print(str1)
