#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#Parent class is the class being inherited from, also called base class.

class Person:
  def __init__(self, fname, lname):
    """
    :param fname: first name of the person
    :param lname: last name of the person
    """
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

obj = Person("Neha", "Sree")
obj.printname()