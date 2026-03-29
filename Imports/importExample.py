# Object Oriented Programming

class MyClass:
    x = 5

class emptyClass:   # Normally, a class cannot be empty, but if you need a class to be empty for come reson call pass
    pass

# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
# The __init__() method is used to assign values to object properties, 
# or to perform operations that are necessary when the object is being created.

class Person:
    # Properties defined inside __init__() belong to each object (instance properties)
    # Properties defined outside methods belong to the class itself (class properties) and are shared by all objects
    species = "Human" 
    def __init__(self, name, age=18):  # Using __init__ allows you to set initial conditions
        self.name = name
        self.age = age
    def greet(self):  # The self parameter is a reference to the current instance of the class. 
       print("Hello, my name is " + self.name) # It is used to access properties and methods that belong to the class.
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")
        
# p2 = Person("Emil", 36)
# print(p2.name)
# print(p2.age)
# p3 = Person("Adam")
# print(p3.name)
# print(p3.age)


# Without the __init__() method, you would need to set properties manually for each object:
class OtherPerson:
    pass

# p4 = OtherPerson()
# p4.name = "Tobias"
# p4.age = 25
# print(p4.name)
# print(p4.age)

class Calculator:   # Class using functions involving parameters
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))

# __str__ is used to determine how to print the class when printed
class printer:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
class printerSTR:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.model} ({self.year})"

# modules can have as many methods/functions as you want
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

# Inheritance
class child:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(child):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)      # super() is used to inherit all of the methods and properties from parent
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

# Encapsulation: Use __ in front of a variable or method to make it priavte
class PrivateTest:
    def __init__(self, parA, parB):
        self.parA = parA
        self.__parB = parB
    
    def getParB(self):
        return self.__parB
    
    def setParB(self, parB):
        self.__parB = parB

    def __validate(self):
        return self.parA < self.getParB()
    
    def grader(self):
        if self.__validate():
            print("A > B")
        else:
            print("B > A")