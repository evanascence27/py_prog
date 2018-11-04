#character identification
ch=input("Enter a character:")
asc=ord(ch)
if asc>=48 and asc<=57:
    print("%c is a digit"%(ch))
elif asc>=65 and asc<=90:
    print("%c is a capital letter"%(ch))
elif asc>=97 and asc<=112:
    print("%c is a small letter"%(ch))
else:
    print("%c is a special symbol"%(ch))
