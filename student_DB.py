#student management system
import sys
import os
import sqlite3 as sql
con=sql.connect("MyApp")
cur=con.cursor()
def Insert():
    ID=input("Enter id:")
    name=input("Enter name:")
    age=input("Enter age:")
    gender=input("Enter gender(M for Male/F for Female):")
    email=input("Enter email:")
    address=input("Enter address:")
    cur.execute("create table if not exists student_record(id int primary key,name varchar(30),age int,gender varchar(1),email varchar(30),address varchar(100))")
    cur.execute("insert into student_record values({},'{}',{},'{}','{}','{}')".format(ID,name,age,gender,email,address))
    con.commit()
    if cur.rowcount >0:
        print("\nRecord inserted successfully")
    else:
        print("\nError in record insertion")
def DeleteID():
    ID=int(input("Enter ID:"))
    cur.execute("delete from student_record where id=%d"%(ID))
    con.commit()
    print("\nRecord delete successfully")
def DeleteAll():
    cur.execute("delete from student_record")
    con.commit()
def DisplayID():
    os.system("cls")
    ID=int(input("Enter ID:"))
    cur.execute("select * from student_record where id=%d"%(ID))
    if len(cur.fetchall())==0:
        print("No such existing record")
    else:
        cur.execute("select * from student_record where id=%d"%(ID))
        print("ID\t\tNAME\t\tAGE\t\tGENDER\t\tE-MAIL\t\t\tADDRESS")
        for j in cur.fetchone():
            print(j,end="\t\t")
        print()
def DisplayAll():
    os.system("cls")
    cur.execute("select * from student_record")
    if len(cur.fetchall())==0:
        print("\nNo existing records")
    else:
        cur.execute("select * from student_record")
        print("ID\t\tNAME\t\tAGE\t\tGENDER\t\tE-MAIL\t\t\tADDRESS")
        for record in cur.fetchall():
            for j in record:
                print(j,end="\t\t")
            print()
def Edit():
    ID=int(input("Enter ID to update:"))
    cur.execute("select * from student_record where id=%d"%(ID))
    if len(cur.fetchall())==0:
        print("No such record found")
    else:
        #cur.execute("select * from student where id=%d"%(ID)) not reqd because we are updating not reading
        name=input("Enter name:")
        age=input("Enter age:")
        gender=input("Enter gender(M for Male/F for Female):")
        email=input("Enter email:")
        address=input("Enter address:")
        cur.execute("update student_record set name='{}',age={},gender='{}',email='{}',address='{}' where id={}".format(name,age,gender,email,address,ID))
        con.commit()
        if cur.rowcount>0:
            print("Record updated")
        else:
            print("Error in record updation")
def main():
    while True:
        os.system("cls")
        print("\t\tSTUDENT MANAGEMENT SYSTEM")
        ch=int(input("\n1.Insert student record\n2.Display record\n3.Delete record\n4.Edit student record\n5.Exit\n\nEnter choice:"))
        if ch==1:
            Insert()
            input("\nPress any key to continue...")
        elif ch==2:
            while True:
                os.system("cls")
                c=int(input("\t1.Display all\n\t2.Display by ID\n\t3.Back to previous menu\n\nEnter choice:"))
                if c==1:
                    DisplayAll()
                elif c==2:
                    DisplayID()
                elif c==3:
                    break
                else:
                    print("Invalid choice")
                input("\nPress any key to continue...")
        elif ch==3:
            while True:
                os.system("cls")
                c=int(input("\t1.Delete all\n\t2.Delete by ID\n\t3.Back to previous menu\n\nEnter choice:"))
                if c==1:
                    DeleteAll()
                elif c==2:
                    DeleteID()
                elif c==3:
                    break
                else:
                    print("Invalid choice")
                input("\nPress any key to continue...")
        elif ch==4:
            Edit()
            input("\nPress any key to continue...")
        elif ch==5:
            break#sys.exit()
        else:
            print("Invalid choice")
            input("\nPress any key to continue...")
    print("\nGOODBYE")
main()
cur.close()

                                                
