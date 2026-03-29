# importing files and modules are important things for programming
import math                         # Imports premade math module
from pathlib import Path            # Used to work with files inside of folders
from Imports import importExample
# When importing a file from another folder, run code using:
# python -m folderName.fileToRunName
# Note: don't end the fileToRunName with .py like you usually would

print(math.sqrt(16))    # Since we have imported the math module, we can use the functions from the math module
print(math.pow(2,3))

folder_path = Path("Imports")
file_path = folder_path / "fileHandle.txt"

# File Handling (Not imbedded in folder)
with open("fileWords.txt", "w") as file:
    file.write("This has been written to the file")

with open('fileWords.txt', 'a') as file:
    file.write("\nNew content appended.")

with open('fileWords.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        print(line, end='')
print()

# File Handling (Imbedding in folder)
Path("Imports/fileHandle.txt").write_text("This has been written to another file")
content = Path("Imports/fileHandle.txt").read_text()
print(content)
with file_path.open(mode='a') as file:
    file.write("\n more text has been added to the file")
content = Path("Imports/fileHandle.txt").read_text()
print(content)
print()

# List files and subdirectories in a folder
for item in folder_path.iterdir():
    if item.is_file():
        print(f"File: {item.name}")
    elif item.is_dir():
        print(f"Directory: {item.name}")
print()

# Self-Made Modules
p1 = importExample.MyClass()    # Makes an object of MyClass called p1, must start with importExample. since the class is from that module
print(p1.x)                     # Prints the x variable of the object
del p1                          # Deletes the object when done
print()

p2 = importExample.Person("Emil", 36)   # From class using __init__
print(p2.name)
print(p2.age)
p3 = importExample.Person("Adam")
print(p3.name)
print(p3.age)
print()

p2.greet()          # using function from class
p3.greet()
print()

print(p2.species)   # using non __init__ variable
print(p3.species)
importExample.Person.species = "Alien"
print(p2.species)
print(p3.species)
print()

p2.celebrate_birthday()     #using functions modifying parameters
p3.celebrate_birthday()
print()

p4 = importExample.OtherPerson()  # From class not using __init__
p4.name = "Tobias"
p4.age = 25
print(p4.name)
print(p4.age)
print()

calc = importExample.Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
print()

printerA = importExample.printer("ModelA", 1981)        # trys to print w/o __str__
printerB = importExample.printerSTR("ModelA", 1981)     # trys to print w/ __str__
print(printerA)
print(printerB)
print()

# Classes with multiple functions
my_playlist = importExample.Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
print()

# Inheritance
child1 = importExample.child("Jerry", "Smith")
student1 = importExample.student("Jared", "Billy", 1982)
child1.printname()
student1.printname()
student1.welcome()
print()

# Polymorphism
car1 = importExample.Car("Ford", "Mustang")         #Create a Car object
boat1 = importExample.Boat("Ibiza", "Touring 20")   #Create a Boat object
plane1 = importExample.Plane("Boeing", "747")       #Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
print()

# Encapsulation
pt = importExample.PrivateTest(10, 4)
pt.grader()
print()