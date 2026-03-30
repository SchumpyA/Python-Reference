# Running Code: 
# To run the program input command: python fileName.py
# If the file in in a folder, run the commad: pythoon folderName/fileName.py

# In Python comments don't use // but instead use #

print("Hello, World!")  # Use print function to print to the terminal, after running it automatically prints endl
print()  # prints a blank line

# Data Types (Integer, Float, String, Bool, etc.) are all automatically assigned based on what is stored

age = 19
name = "Adam"
alive = True  # True and False must be capitalized
dead = False

print(name)  # Variables can be put into the print function to print the variable
print(age)
print(alive)
print(dead)
print()

# Use casting to force a specific data type on a variable
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x,y,z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z,w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)


# Input
# Use input command to take input from terminal, the test inside the parameter is printed before taking the input
name = input("Enter Name: ")
print(name)
print()

# Operators and Expressions

x = 1
y = 2
z = 10

print(x,y,z) # to print multiple variables or split up text, use commas as you would +'s in c++
print()

a = x + y   # addition
b = z - x   # subtraction
c = z * y   # multiplication
d = z / y   # division
e = z // 3  # floored-division
f = z % 3   # modulo

print("Addition: " , a , "\nSubtraction: " , b , " \nMultiplication" , c , " \nDivision" , d , "\nFloored Division" , e , "\nModulo" , f)
print()

# == for equal, != for not equal, < and > for regular purpose, and for &&, not for !, or for ||

# Control Flow

# If-Statements:
x = input("Give Number: ")
y = input("Give Number: ")
z = input("Give Number: ")
if x >= z and x >= y:
    print(x, "Is the Largest")
elif y >= z and y >= x:
    print(y, "Is the Largest")
else:
    print(z, "Is the Largest")
print()

# Loops:
for i in range(5):
    print(i)

x = 5
while x > 0:
    x-= 1
    print(x)
print()

# Functions

# Defining a basic function
a = 10
b = a/2
def add(a, b):
    return a + b

# Default and Keyword Arguments
def greet(name="Guest)"):
    print(name)
print()

# Lambda Functions
# A lambda function in Python is a small, anonymous function defined using the lambda keyword 
# that can take any number of arguments but is restricted to a single expression. 
# The result of the expression is automatically returned, without needing a return keyword.
x = 5
square = lambda x: x*x

# Data Structures

# Lists
# Lists are mutable(changeable), Ordered(insertion order is maintained), allows duplicates, and supports indexing and slicing
nums = [1,2,3,2]
nums.append(4)
print(nums)
print(len(nums))   # len() returns the number of items in the list/tuple/set

# Tuples
# Tuples are just like lists, except they are immutable (cannot be changed after initialization)
t = (1,2,3)
print(t)
print(len(t))   # len() returns the number of items in the list/tuple/set

# Sets
# Sets are mutable, unordered (no guarenteed order), don't allow duplicates, and don't support indexing
s = {1,2,3,3,5,23, 12}
print(s)
print(len(s))   # len() returns the number of items in the list/tuple/set

# Dictionaries
# a built-in, mutable data structure that stores data in key-value pairs.
# It is used to associate a specific value with a unique key,
# allowing for efficient data retrieval (average O(1) performance) using that key instead of a numeric index
# Creating a dictionary using curly braces {}
user_profile = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing a value using its key
print(user_profile["name"]) # Output: Alice

# Printing full dictionary
print(user_profile)

# Modifying an existing value
user_profile["age"] = 31

# Adding a new key-value pair
user_profile["email"] = "alice@example.com"

# Deleting a key-value pair
del user_profile["city"]
print(user_profile)
print(len(user_profile))    # For dictionaries len() returns the number of key/value pairs in the dictionary
print()

# Error Handling
try:
    a = int(input("Input Number: "))
except:
    print("Invalid input")