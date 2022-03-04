# parent class constructor getting called
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is  {}".format(self.name))
        print("My id number is {}".format(self.idnumber))
        print("In the parent class")

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My id number is {}".format(self.idnumber))
        print("post {}".format(self.post))

a = Employee("Rahul", 886021, 20000, "Intern")

a.display()
a.details()
man = Person("dev", 'Engg')
Person.details(man)