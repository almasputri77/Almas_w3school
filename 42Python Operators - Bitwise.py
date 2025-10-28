# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator  Name	                Description	                                    Example	
# & 	    AND	                    Sets each bit to 1 if both bits are 1	        x & y	
# |	        OR	                    Sets each bit to 1 if one of two bits is 1	    x | y	
# ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	        NOT	                    Inverts all the bits	                        ~x	
# <<	    Zero fill left shift	Shift left by pushing zeros in from the right   x << 2
#                                   and let the leftmost bits fall off	            	
# >>	    Signed right shift	    Shift right by pushing copies of the leftmost   x >> 2
#                                   bit in from the left, and let the rightmost 
#                                   bits fall off	

# Example
print(6 & 3)
# Bit akan jadi 1 hanya jika kedua bit bernilai 1.
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
#                                   0010, which is 2 in decimal


# Example
print(6 | 3)
# Bit akan jadi 1 jika salah satu bit bernilai 1.
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
#                                   0111, which is 7 in decimal.

# Example
print(6 ^ 3)
# Bit akan jadi 1 hanya jika salah satu bit bernilai 1, tapi bukan keduanya.
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011
#                                   0101, which is 5 in decimal.


