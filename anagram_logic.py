#anagram logic
str1=input("string:")
str2=input("string:")
for i in range(len(str1)):
    if str2[i] not in str1:
        print("NOT ANAGRAM")
        break
else:
    print("ANAGRAM")
        
