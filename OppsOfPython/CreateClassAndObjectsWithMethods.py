class Dog:
    # class attribute
    attr1 = "mammal"

    # instance Attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

    # driver code
    # object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.speak()
Tommy.speak()

Dog.speak(Rodger)

