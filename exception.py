#exception
try:
    x=int(input("Enter number:"))
    y=int(input("Enter number:"))
    print(x/y)
except ValueError:
    print("Invalid input(Enter integer only)")
except ZeroDivisionError:
    print("Division by 0 not possible")
except:
    print("Error!!!")
else:
    print("Bye Bye")
finally:
    print("Hello")
