#maths quiz
import sys
import random as r
c=0
def menu():
    global c
    print("*******************")
    print("*Simple Maths Quiz*")
    print("*******************")
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        try:
            choice=int(input("Enter choice:"))
        except ValueError:
            print("Please enter an integer.")
            continue
        a=r.randrange(30)
        b=r.randrange(30)
        if choice==1:
            add(a,b)
        elif choice==2:
            sub(a,b)
        elif choice==3:
            mul(a,b)
        elif choice==4:
            div(a,b)
        elif choice==5:
            print("Your score is:%d"%(c))
            sys.exit()
        else:
            print("Invalid choice.")
def add(a,b):
    exp=("{}+{}".format(a,b))
    ans=int(input(exp+"="))
    if ans==int(eval(exp)):
        print("correct")
        score()
    else:
        print("incorrect")
def sub(a,b):
    exp=("{}-{}".format(a,b))
    ans=int(input(exp+"="))
    if ans==int(eval(exp)):
        print("correct")
        score()
    else:
        print("incorrect")
def mul(a,b):
    exp=("{}*{}".format(a,b))
    ans=int(input(exp+"="))
    if ans==int(eval(exp)):
        print("correct")
        score()
    else:
        print("incorrect")
def div(a,b):
    exp=("{}/{}".format(a,b))
    ans=float(input(exp+"="))
    if ans==float(eval(exp)):
        print("correct")
        score()
    else:
        print("incorrect")
def score():
    global c
    c+=1
menu()
