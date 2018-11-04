#atm machine
import sys
import getpass
import os
print("4 users enter their atm pin:")
d={}
for i in range(2):
    d1={input("Enter account number:"):{input("Enter pin:"):{input("Enter name:"):int(input("Enter balance:"))}}}
    d.update(d1)
while 1:
    os.system("cls")
    acc=input("Enter account number:")
    pin=getpass.getpass(prompt="Enter pin:")
    for j in d.items():
        for k in j[1].items():
            if k[0]==pin:
                os.system("cls")
                choice=int(input("1.Withdrawal\n2.Deposit\n3.Minimum Balance\n4.Exit"))
                if choice==1:
                    os.system("cls")
                    for i in d[acc][pin].items():
                        name=i[0]
                    print("NAME:",name)
                    draw=int(input("Enter amount to withdraw:"))
                    d[acc][pin][name]-=draw
                    print("Please collect your cash.")                     
                elif choice==2:
                    os.system("cls")
                    for i in d[acc][pin].items():
                        name=i[0]
                    print("NAME:",name)
                    dep=int(input("Enter amount to withdraw:"))
                    d[acc][pin][name]+=dep
                    print("Amount has been deposited.")                     
                elif choice==3:
                    os.system("cls")
                    for i in d[acc][pin].items():
                        name=i[0]
                    print("NAME:",name)
                    print("ACCOUNT NUMBER:",acc)
                    print("BALANCE:",d[acc][pin][name])
                elif choice==4:
                    sys.exit()
                else:
                    print("Invalid choice.")
            else:
                os.system("cls")
                print("Account does not exist.")
                break
            print("Thank you.")
            input("Press any key to continue...")

