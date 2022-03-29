class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute It is run as soon as an object of a class is instantiated.
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()
