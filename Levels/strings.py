# String Handling

# Indexing and Slicing
text = "Hello"
print(text)
print(text[0])      # 'H'
print(text[-1])     # 'o'
print(text[1:4])    # 'ell'
print(text[::-1])   # reverse
print()

# len is used to find length of a string
textLength = len(text)
print(textLength)
print()

# Important methods
sentence = " I! Like! Food!!"
print(sentence.upper() )                    # Makes string all uppercase
print(sentence.lower())                     # Makes string all lowercase

print(sentence.strip())                     # Removes whitespace on the edges of the string
print(sentence.strip("!"))                  # Removes input character/string on the edges of te string

print(sentence.replace("Like", "Hate"))     # Replaces part of string with somthing else

print(sentence.split())                     # Splits string into substrings via whitespace
print(sentence.split("!"))                  # Splits string into substrings via input character(s)
print(sentence.split("!", maxsplit=2))      # Splits string into substrings with a max of x splits

print(",".join(["a", "b"]))                 # Joins two substrings together with input character(s) inbetween
print()

# An f-string (formatted string literal) is a string formatting mechanism
# which provides a concise and readable way to embed Python expressions directly
# within a string literal for dynamic content creation

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.

goldenRatio = (1 + 5**0.5) / 2
print(f"{goldenRatio=}")  # Output: goldenRatio=1.618033988749895
print()

# .format() replaces parts of the string with inputs character(s)

# Using bare {} just goes through the parameters in order
print("We are the {} who say '{}!'".format('knights', 'Ni'))  # Output: We are the knights who say 'Ni!'

# Using numbered {} picks a specific parameter
print("{1} and {0}".format('spam', 'eggs'))  # Output: eggs and spam

# Using veriabled {} picks a specific parameter
print("This {food} is {adjective}.".format(food='spam', adjective='absolutely horrible'))  # Output: This spam is absolutely horrible.
print()

# Both f-strings and the .format() method use a common format specification mini-language after a colon : within the curly braces. 
pi = 3.1415926
print(f"Pi is approximately {pi:.2f}.") # Formats float to 2 decimal places # Output: Pi is approximately 3.14.

num = 13
print(f"|{num:10d}|")   # Right aligned within 10 characters (default for numbers)
print(f"|{num:<10d}|")  # Left aligned within 10 characters
print(f"|{num:^10d}|")  # Center aligned within 10 characters
print(f"|{num:04d}|")   # Pad with zeros to a width of 2

large_num = 1000000
print(f"Formatted number: {large_num:,}.") # Uses a comma as a thousands separator # Output: Formatted number: 1,000,000

# Old Style % formating replaces parts of the string based on % and letter after, %s means string and %d means integer
name = "Joanna"
age = 42
print("My name is %s and I am %d years old." % (name, age)) # Output: My name is Joanna and I am 42 years old.
print()

# \n is for newline, \t is for tab
print("N is for \n making a \n new line")
print("T is for \t making a \t tab in between")
print()

# A raw string literal is a string literal prefixed with the letter r or R.
# This tells the interpreter to treat backslashes (\) as literal characters rather than escape sequence indicators
print(r"No \n More \n New Lines")