# Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator	    Example     Same As
# =	            x = 5       x = 5	
# +=	        x += 3	    x = x + 3	
# -=	        x -= 3	    x = x - 3	
# *=	        x *= 3	    x = x * 3	
# /=	        x /= 3	    x = x / 3	
# %=	        x %= 3	    x = x % 3	
# //=	        x //= 3	    x = x // 3	
# **=	        x **= 3	    x = x ** 3	
# &=	        x &= 3	    x = x & 3	
# |=	        x |= 3	    x = x | 3	
# ^=	        x ^= 3	    x = x ^ 3	
# >>=	        x >>= 3	    x = x >> 3	
# <<=	        x <<= 3	    x = x << 3	
# :=	        print(x := 3)	x = 3
#                             print(x)

# The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

# Example
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

