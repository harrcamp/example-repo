import os
os.system('cls' if os.name == 'nt' else 'clear')

# print the first row of stars

start_number = 1 
stars = "*"

if start_number == 1: # the variable above returns True 
    for i in range(0, 5): # set the maximum range of stars
        print(stars) 
        stars = stars + "*" # add a star for each row
    for i in range(0, 3): 
        index = 4 - i  # reduce the number of stars by 1 each row
        print(stars[0:index])


""" # computer output 
           
start_number = 1
max_rows     = 5 # height of the upward part (the peak)

# total lines = upward lines + downward lines (everything below the peak)
total_lines  = max_rows + (max_rows - 2)   # 5 + 3 = 8

if start_number == 1:
    for line in range(0, total_lines):
        # decide how many stars this line gets
        stars_this_line = line if line <= max_rows else total_lines - line + 1
        print('*' * stars_this_line)
 """

# model answer

""" # The number of rows for the pattern.
rows = 10


# Check if 'rows' is an even, positive integer greater than zero.
if (rows // 2) * 2 == rows and rows > 0:
    # Initialise Variables
    count = 0
    asterisk = "*"
    half = rows//2


    for index in range(1, rows):
        # Increment the half of the pattern
        if index <= half:
            count += 1


        # Decrement the half of the pattern
        else:
            count -= 1


        # Print asterisks
        print(asterisk * count)


else:
    # If an invalid number has been entered print an error message.
    print("Invalid input.Please enter an even positive integer for 'rows.")
 """