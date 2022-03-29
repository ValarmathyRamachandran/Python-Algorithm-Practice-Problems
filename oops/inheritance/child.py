class Person:
  def __init__(self, fname, lname):
    """
    :param fname: first name of the person
    :param lname:  last name of the person
    """
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print (self.firstname, self.lastname)

# it will inherit the properties and methods from the Person class:
class Student(Person):
  pass
#Use the pass keyword when you do not want to add any other properties or methods to the class.

obj = Student("Valarmathy", "Ramachandran")
obj.printname()