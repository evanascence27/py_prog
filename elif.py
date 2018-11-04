#else if
marks=int(input("Enter marks of student:"))
if marks>=80:
    print("A+ grade")
elif marks>=70 and marks<80:
    print("A grade")
elif marks>=60 and marks<70:
    print("B+ grade")
elif marks>=50 and marks<60:
    print("B grade")
else:
    print("C grade")
