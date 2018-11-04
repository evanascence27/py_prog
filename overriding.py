#overriding
class Employee:
    def Display(self):
        print("Employee")
class Student(Employee):
    def Display(self):
        super().Display()
        print("Student")
ob=Student()
ob.Display()

