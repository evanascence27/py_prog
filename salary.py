basic=int(input("Enter basic salary:"))
if basic<=2000:
    da=10
    hra=20
elif basic>2000 and basic<=5000:
    da=20
    hra=30
elif basic>5000 and basic<=10000:
    da=30
    hra=40
else:
    da=50
    hra=50
da=da/100*basic
hra=hra/100*basic
print("BASIC=%d\nDA=%lf\nHRA=%lf"%(basic,da,hra))
