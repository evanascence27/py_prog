#inheritance
class Employee:
    def  __init__(self):
        self.__id=10
        self._name="ABC"
        self.salary=100
class Student(Employee):
    def Display(self):
        #print(self.__id) unavailable to object
        print(self._name)
        print(self.salary)
ob=Student()
ob.Display()
print(ob._name,ob.salary)#both unavailable to object
