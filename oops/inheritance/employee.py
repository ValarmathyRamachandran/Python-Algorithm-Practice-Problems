# A Python program to demonstrate inheritance

class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return "is not employee"


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return "is a employee"


if __name__ =="__main__":
    emp = Person("Mike")  # An Object of Person
    print(emp.getName(), emp.isEmployee())

    emp = Employee("Ben")  # An Object of Employee
    print(emp.getName(), emp.isEmployee())
