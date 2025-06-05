import math

# Ask the user to input three integers and store in
# three different variables
integer1 = input("Enter an integer: ")
integer2 = input("Enter a second integer: ")
integer3 = input("Enter a third integer: ")

# sum the numbers
print(int(integer1) + int(integer2) + int(integer3))

# first number minus 
print(int(integer1) - int(integer2))

# third number multiplied by the first number
print(int(integer3)*int(integer1))

# sum of three numbers divided by third number
print(((int(integer1) + int(integer2) + int(integer3))/(int(integer3))))

# Note you can just divide the numbers without 
# peren using only operators for cleaner code

# Store calculations as variables then print 
# everything with a label at the end