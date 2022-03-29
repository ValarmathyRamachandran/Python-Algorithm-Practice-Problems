# Python example to show the working of multiple inheritance
# When a child class inherits from multiple parent classes, it is called multiple inheritance.
class Base1(object):
    def __init__(self):
        self.str1 = "Hello"
        print("Base1")



class Base2(object):
    def __init__(self):
        self.str2 = "Everyone"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)

if __name__ == "__main__":
    ob = Derived()
    ob.printStrs()
