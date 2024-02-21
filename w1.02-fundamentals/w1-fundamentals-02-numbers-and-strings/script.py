"""
PRIMITIVE (SIMPLE) DATATYPES
- Strings (str)
- Integers (int)
- Floating Point Numbers (float)
- Booleans (bool)
- None (NoneType)
"""

"""
=== === Strings === ===
Strings represent sequences of characters enclosed
in quotes.
"""
# String creation:
# snake_case

# variable name rules
# can't start with a number
# can't have a hyphen
# can't use reserved keywords

# Literal assignment
my_greeting = "hello world"

# Constructor function (casting)
greeting_2 = str("Another greeting")

# Print function
print(my_greeting)

# Type function
print(type(my_greeting))

# Concatenation
hello = "hello"
world = "world!"

hello_world = hello + " " + world
print(hello_world)

# f-string
print(f"{hello} big {world}")
print(hello + " " + "big" + " " + world)

# TypeError
num = 10
sentence = "my age is "
# print(sentence + num)
# Fix
print(sentence + str(num))

print(type(str(num)))

# String Methods
# `rsplit()` splits a string based on a separator
stack = "Python world"
print([*stack])

# upper, lower, title
print(stack.upper())
print(stack.lower())
print(stack.title())

print(stack.center(50, "*"))

# length
print(len(stack))

# strip
whitespace_string = "      hello          "
print(whitespace_string)
print(whitespace_string.strip())

# string indices, index ranges
guitar = "fender"
print(guitar[0])
# slicing with index ranges
print(guitar[:3])
# negative index
print(guitar[-2])

# Explore more string methods!
# https://www.w3schools.com/python/python_ref_string.asp

"""
=== === BOOLEANS === ===
Booleans represent the value of True or False.
"""

# Literal assignment

# snake case - every letter is lowercase and
# every word is separated by an underscore

# Constructor function (casting)

# Logical operators tomorrow

"""
=== === INTEGERS AND FLOATS === ===
Integers represent whole numbers. Floats represent
decimal numbers.
"""

# Integer literal assignment

# Constructor function (casting)

# Float literal assignment

# Constructor function (casting)

# Arithmetic operations
# +, -, *, /, **, //

# +=, -=, *=, /= assignment operators

# Built-in functions for numbers

# abs, round

# Math module

# sqrt, ceil, floor

"""
=== === NONE === ===
None represents the absence of a value.
"""
# None literal assignment

# Why use None?
