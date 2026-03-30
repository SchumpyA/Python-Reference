# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# W/O List Comprehension
# Best to use for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print()

# With list comprehension you can do all that with only one line of code
# Syntax:
# newlist = [expression for item in iterable if condition == True]
places = ["Library", "Zoo", "School", "House", "Cemetary"]

newlistLCa = [x for x in places if "a" in x]
newlistLCo = [x for x in places if "o" in x]

print(newlistLCa)
print(newlistLCo)

# Can use boolean operations in the expression
newListLCNOe = [x for x in places if "e" not in x]
print(newListLCNOe)
print()

# For this you can use iterables like range()
newNumList = [x for x in range(11) if x < 5 or x == 10]
print(newNumList)
print()

# How to manipulate input value
food = ["Bread", "Pizza", "Cake", "Chocolate"]
newFoodListA = [x.upper() for x in food]                        # Adds in all of the options in upercase
newFoodListB = ["hello" for x in food]                          # Adds in input string for every oprion
newFoodListC = [x if x != "Bread" else "orange" for x in food]  # Replaces a specific value with another specific value
print(newFoodListA)
print(newFoodListB)
print(newFoodListC)
print()

# Nested
nestedList = [(x,y) for x in range(5) for y in range(3)]
print(nestedList)
print()

# Extra
addition = [x+x for x in range(5)]        # 0+0, 1+1, 2+2, ... , (n-1) + (n-1)
multiplication = [x*x for x in range(5)]  # 0*0, 1*1, 2*2, ... , (n-1) * (n-1)
print(addition)
print(multiplication)
