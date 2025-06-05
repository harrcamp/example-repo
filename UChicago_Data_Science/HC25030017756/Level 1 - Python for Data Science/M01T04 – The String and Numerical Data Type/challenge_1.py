import os
os.system('cls' if os.name == 'nt' else 'clear')

# import math module

import math

# request the user to enter three side of a triangle
s_1 = int((input("Enter the length of one side of a triangle: ")))
s_2 = int((input("Enter the length of second side of the triangle: ")))
s_3 = int((input("Enter the length of third side of the triangle: ")))

## print(type(s_1))

# calculate semi-perimiter of the triangle
s_p = int(int(s_1) + int(s_2) + int(s_3)) / (2)

# sqr.root of the product of the difference between each  side and semi-perimeter
area_triangle = round(float(math.sqrt(
    (s_p) * (s_p-s_1) * (s_p-s_2) * (s_p-s_3))), 3)
print(area_triangle)

# yada yada update terminal commit test command entry