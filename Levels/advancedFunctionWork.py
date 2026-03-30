# Arbitrary arguments *args

# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print()

def my_second_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_second_function("Computer", 12, 1.34, True, "This is a sentence.")
print()

# You can combine regular parameters with *args
# Regular parameters must come before *args

def my_third_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_third_function("Hello", "Emil", "Tobias", "Linus")
print()

# Example of practical use: (finds sum of inputs)
def addition(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(addition(1, 2, 3))
print(addition(10, 20, 30, 40))
print(addition(5))
print()

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly

def lastNames(**kid):
    print("His last name is " + kid["lname"])

lastNames(fname = "Tobias", lname = "Refsnes")
print()

def printPeople(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

printPeople(name = "Tobias", age = 30, city = "Bergen")
print()

# You can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs:
def printUser(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

printUser("emil123", age = 25, city = "Oslo", hobby = "coding")
print()

# To use *args and **kwargs, follow the order 1. regular parameters 2. *args 3. *kwargs
def allArgs(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

allArgs("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
print()

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments

# Example with * (used for lists)
def nums(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = nums(*numbers)  # Same as: nums(1, 2, 3)
print(result)
print()

# Example with ** (used for dictionaries)
def nameFunction(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
nameFunction(**person)  # Same as: my_function(fname="Emil", lname="Refsnes")
print()

# Decorators let you add extra behavior to a function, without changing the function's code
# A decorator is a function that takes another function as input and returns a new function
# Define the decorator first, then apply it with @decorator_name above the function

def changeCaseUpper(func):       # This will be the decorator
    def myinner():
        return func().upper()
    return myinner

@changeCaseUpper
def addedFunction():        # This is the function that will be decorated
    return "Hello Sally"    # Will print HELLO SALLY since the original has .upper()

@changeCaseUpper
def otherAddedFunction():   # This is another function that will be decorated
    return "I am speed!"      # Will print I AM SPEED! for same reason

print(addedFunction())
print(otherAddedFunction())
print()

# Functions that require arguments can also be decorated,
# just make sure you pass the arguments to the wrapper function

def changeCaseLower(func):
    def myinner(x):
        return func(x).lower()
    return myinner

@changeCaseLower
def hello(name):
    return "Hello " + name

print(hello("John"))
print()

# Sometimes the decorator function has no control over the arguments passed from decorated function, 
# to solve this problem, add (*args, **kwargs) to the wrapper function, 
# this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

def addOne(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs) + 1
    return myinner

@addOne
def myNum(num):
    return num

print(myNum(10))
print()

# Decorators can accept their own arguments by adding another wrapper level.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def greet():
  return "Hello Linus"

@changecase(0)
def farewell():
    return "Bye Linus"


print(greet())
print(farewell())
print()

# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function.

def addgreeting1(func):
    def myinner():
        return "Hello " + func()
    return myinner

def addgreeting2(func):
    def myinner():
        return "Brother " + func()
    return myinner

def addfarewell(func):
    def myinner():
        return func() + " Have a good day!"
    return myinner

@addfarewell
@addgreeting1
@addgreeting2
def talk1():
    return "Tobias"  # Will print "Hello Brother Tobias Have a good day"

@addfarewell
@addgreeting2
@addgreeting1
def talk2():
    return "Fred"    # Will print "Brother Hello Fred Have a good day"

print(talk1())
print(talk2())