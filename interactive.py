########################
# This program will read in
# user input by using the
# input () function in python.
# We can store the user input
# in a variable and manipulate
# it.
#
########################

# the addition functionality of our calc

x1 = float(input("Enter in a number to add "))
print("The number entered is ", x1)

y1 = float(input("Enter in another number to add "))
print("The second number is ", y1)

print(x1, '+', y1, '=', x1 + y1) # sum numbers x and y

# the subtraction functionality of our calc

x2 = float(input("Enter in a number to subtract "))
y2 = float(input("Enter in the second number "))
print(x2, '-', y2, '=', x2 - y2)

# the multiplication functionality of our calc

x3 = float(input("Enter in a number to multiply "))
y3 = float(input("Enter in another number to multiply "))
print(x3, '*', y3, '=', x3 * y3)

# the division functionality of our calc

x4 = float(input("Enter in a number to divide "))
y4 = float(input("Enter in another number to divide "))
print(x4, '/', y4, '=', x4 / y4)

# implement the power functionality using **

x5 = float(input("Enter in a number to increase to a power "))
y5 = float(input("Enter the power value "))
print(x5, '**', y5, '=', x5 ** y5)

# implement the mod functionality %

x6 = float(input("Enter in a number "))
y6 = float(input("Enter a number to find the modulus value "))
print(x6, '%', y6, '=', x6 % y6)

# implement the math module, and implement ANY one functionality

import math

x7 = float(input("Enter a number you would like to get the square root "))
print(math.sqrt(x7))

# Create a GitHub account

