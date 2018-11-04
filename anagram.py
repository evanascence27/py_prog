#anagram
str1=input("enter string 1:")
str2=input("enter string 2:")
str1=str1.upper()
str2=str2.upper()
s1='\0';s2='\0'
for i in range(65,113):
    if chr(i) in str1:
        s1+=chr(i)
    if chr(i) in str2:
        s2+=chr(i)
if s1==s2:
    print("ANAGRAM")
else:
    print("NOT")
