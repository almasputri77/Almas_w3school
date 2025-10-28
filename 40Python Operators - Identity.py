# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

# Operator	Description	                                            Example	
# is 	    Returns True if both variables are the same object	    x is y	
# is not	Returns True if both variables are not the same object	x is not y

# Example
# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# Example
# The is not operator returns True if both variables do not point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
# Example
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
