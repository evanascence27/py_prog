#fibonacci
s1=1;s2=0;s3=0
while 1:
    s3=s1+s2
    if(s3>50):
        break
    print(s3)
    s1=s2
    s2=s3
