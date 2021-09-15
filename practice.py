name = "genesis"
age = 27

print(name)
print(age)

def printer():
    print("Hello")

def namePrinter(personsName):
    print(personsName)


def admitted(name):
    if(name == "Genesis"):
        print("Admitted")
    else:
        print("not admitted")

admitted("Genesis")
admitted("Markos")

class Dog: 
    def __init__(self, name, owner, age):
        self.name = name
        self.owner = owner
        self.age = age 
    def printName(self):
        print(self.name)

dog1 = Dog("Louie", "Raquel", 7)
dog2 = Dog("Buddy", "Alazar", 5)
print(dog1.name)
print(dog2.name)
print(dog1.owner)
dog1.printName()

