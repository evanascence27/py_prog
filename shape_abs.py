#shapes using area
import os
import sys
from abc import *
class Shape(ABC):
    @abstractmethod
    def input(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Triangle(Shape):
    def input(self):
        self.b=int(input("Base length of triangle:"))
        self.h=int(input("Height of triangle:"))
    def area(self):
        return .5*self.b*self.h
class Square(Shape):
    def input(self):
        self.a=int(input("Side of square:"))
    def area(self):
        return self.a*self.a
class Rectangle(Shape):
    def input(self):
        self.l=int(input("Length of rectangle:"))
        self.b=int(input("Breadth of triangle:"))
    def area(self):
        return self.b*self.l
def menu():
    while True:
        print("1.Triangle\n2.Square\n3.Rectangle\n4.Exit")
        choice=int(input("Enter choice:"))
        if choice==1:
            ob=Triangle()
            ob.input()
            print("Area of triangle: ",ob.area())
        elif choice==2:
            ob=Square()
            ob.input()
            print("Area of square: ",ob.area())
        elif choice==3:
            ob=Rectangle()
            ob.input()
            print("Area of rectangle: ",ob.area())
        elif choice==4:
            print("GOODBYE")
            #os.system("exit")
            sys.exit()
        else:
            print("Invalid choice")
menu()
