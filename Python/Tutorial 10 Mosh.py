#09/01/2022 
#Constructors
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

#10/01/2022
#Inheritance
class Mamal:
    def walk(self):
        print("walk")

class Dog(Mamal):
    def bark(self):
        print("bark")

class Cat(Mamal):
    pass

#Modules
