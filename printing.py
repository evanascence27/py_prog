#divisibility by 7 not by 5
for x in range(2000,2101):
    if(x%5==0):
        continue
    if(x%7==0):
        print(x,end=',')
