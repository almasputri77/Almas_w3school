# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	                                                                        Example	
# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# Example
# Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

# Example
# Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

# Membership in Strings
# The membership operators also work with strings:

# Example
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

