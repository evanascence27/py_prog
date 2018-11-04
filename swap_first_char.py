#swap first character of each word
str=input("enter full name:")
i=str.index(" ")
print(str[i+1]+str[1:i])
print(str[0]+str[i+2:])
