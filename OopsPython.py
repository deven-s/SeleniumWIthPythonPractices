class Vehicle:

    numberOfWheels = None
    def printNumOfWheels(self):
        print("numebr of wheels = ", self.numberOfWheels)

class twoV(Vehicle):
    def __init__(self, wheels):
        Vehicle.numberOfWheels = wheels


class fourV(Vehicle):
    def __init__(self, wheels):
        Vehicle.numberOfWheels = wheels


obj2 = twoV(2)

obj2.printNumOfWheels()

obj4 = fourV(4)

obj4.printNumOfWheels()