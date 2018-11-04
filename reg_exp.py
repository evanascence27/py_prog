#reading data from file using reg exp
import re
import time
import os
fp=open("regexp.txt","r")
s=fp.read()
fp.close()
while True:
    os.system("cls")
    print("1.Display all phone numbers")
    print("2.Display all email IDs")
    print("3.Display all IP address")
    print("4.Display all names")
    print("5.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        phone_list=re.findall("\d{10}",s)
        for i in phone_list:
            print(i)
    elif choice==2:
        email_list=re.findall(r"[\w]+@[\w]+\.\w{2,4}",s)
        for i in email_list:
            print(i)
    elif choice==6:
        email_list=re.findall(r"[\w]+@yahoo+\.\w{2,4}|[\w]+@hotmail+\.\w{2,4}",s)
        for i in email_list:
            print(i)
    elif choice==3:
        ip_list=re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
        for i in ip_list:
            print(i)
    elif choice==4:
        fp=open("regexp.txt","r")
        s=fp.readline()
        while s:
            print(re.match(r"[\w],",s))
            s=fp.readline()
        fp.close()
    elif choice==5:
        break
    time.sleep(3)


    
