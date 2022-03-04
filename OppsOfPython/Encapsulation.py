class Base:
    def __init__(self):
        self.a = "GeeksForGeeks"
        self.__c = "GeekForGeeks"


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class")
        print(self.__c)


obj = Base()

print(obj.a)
