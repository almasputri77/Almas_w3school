# Get the Length of a Set
# To determine how many items a set has, use the len() function.

# Example
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type:

# Example
# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:

# Example
# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

# type()
# From Python's perspective, sets are defined as objects with the data type 'set':

# <class 'set'>

# Example
# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Example
# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


