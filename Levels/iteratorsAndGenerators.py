# An iterator is an object that contains a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values

# Example, iterating through a tuple
mytuple = ("apple", "banana", "cherry", "durian")
myit = iter(mytuple)

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry
print()            # durian is not iterated to, so it is not printed

# Example, iterating through a string
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # b
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a
print(next(myit))  # n
print()            # the final a is not iterated to, so it is not printed

# Example, creating an iterator, and including a stop to the iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))   # 1
print(next(myiter))   # 2
print(next(myiter))   # 3
print(next(myiter))   # 4
print(next(myiter))   # 5
for x in myiter:
    print(x)          # prints from 1 to 10 (when iterator is stopped)
print()

# Python generators are a simple and memory-efficient way to create iterators that produce values one at a time,
# without storing the entire sequence in memory.
# They are especially useful for handling large or infinite data stream
def count_up_to(max):
    n = 1
    while n <= max:
        yield n
        n += 1

# Using the generator
counter = count_up_to(5)
for num in counter:
    print(num)
print()

# A generator expression that yields the square of numbers
squares_generator = (i * i for i in range(5))

# Iterate through the generated values
for square in squares_generator:
    print(square)
print()