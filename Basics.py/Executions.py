# Expression Executions

# String and numeric value can operate together with * 
A, B = 1,2
text = "@"
print(A* text * B)
# output will be @@


# String and string can operate with * 
C , D = '3' , 4
print((C + text) * D )
# output will be 3@3@3@3@ 


# Numeric values can operate with arithmetic operators
E, F = -5,6
print(A+B*D)
# output will be 9 


# Arithmetic expression with integer and float will result in float 
G = 22.3
print (B * G)
# output will be 44.6


# Result of division operator with 2 integers will be float
print( B/D)
# output will be 0.5


# Integer division(floor) with float and integer will give integer displayed as float 
print(G//B , G/B)
print (E//F)
# output wil be 11.0  , 11.15
# output has to be 0.83 but it is -1 beoz floor gives closet integer value which is lesser than or equal to float value 


# Reminder or modulo 
# num     +   +   -   -
# deno    +   -   -   +
# answer  +   -   +   +
print(E%D)
# output has to be -3 but it is 3




