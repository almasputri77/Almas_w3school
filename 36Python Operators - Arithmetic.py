# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	            Name	    
# +	Addition	        x + y	
# -	Subtraction	        x - y	
# *	Multiplication	    x * y	
# /	Division	        x / y	(pembagian hasil float (decimal))
# %	Modulus	            x % y	(sisa pembagian)
# **	Exponentiation	x ** y	(pangkat)
# //	Floor division	x // y  (pembagian hasil integer)

# Example
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Tanda % di Python disebut operator modulus (modulo).
# Fungsinya adalah untuk menghasilkan sisa pembagian dari dua angka.
print(8 % 2)   # 0, karena 8 habis dibagi 2
print(9 % 2)   # 1, karena 9 dibagi 2 sisanya 1
print(17 % 5)  # 2, karena 17 = 3*5 + 2

# Division in Python
# Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)
# Example
# Division always returns a float:
x = 12
y = 5

print(x / y)

# Example
# Floor division always returns an integer.

# It rounds DOWN to the nearest integer:

x = 12
y = 5

print(x // y)