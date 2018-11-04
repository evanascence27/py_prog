str=input("enter string:")
if len(str)<2:
    print(str)
else:
    print(str[:2]+str[-2:])
