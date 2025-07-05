"""
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
"""
import math

# PART 1 & 2

# taking in user input x and y
x = int(input("Enter a number:"))
y = int(input("Enter another number: "))

# PART 3 & 4
print("X**y = ", x ** y)
print("log(x) =", math.log(x,2))

