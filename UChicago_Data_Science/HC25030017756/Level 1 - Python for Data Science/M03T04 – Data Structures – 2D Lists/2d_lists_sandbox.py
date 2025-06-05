""" # Initialize vairables for the specific size of the grid
# In this case we have a 3 by 2 grid
number_of_rows = 3
number_of_columns = 2

# Create the None vaslues twice in a list of the columns
# then employ a loop to do it three times for the number of rows
empty_grid = [[None] * number_of_columns for _ in range(number_of_rows)]

print(empty_grid)
# Printing this grid will give the following output
# [[None, None], [None, None], [None, None]]

table[1][0] = 4 # table[row 2][column 1]
""" 
""" grayscale_image = [[236,  189, 189,   0],
                   [236,   80, 189, 189],
                   [236,    0, 189,  80],
                   [236,  189, 189,  80]]

last_pixel = grayscale_image[3][3]
""" 
student_score = [[72, 85, 87, 90, 69],
                 [80, 87, 65, 89, 85],
                 [96, 91, 70, 78, 97],
                 [90, 93, 91, 90, 94]]

# Use a for loop to print all elements of the two-dimensional array
row_index = 0
for row in student_score:  # Outer loop for rows
    print(f'Term {row_index + 1}: ')
    row_index += 1 # Increment row index
    for col in row: # Inner loop for columns
        print(col, end = "% ") # print each colum value with a % symbol
    print()  

""""
ragged_list = [[ 1, 2, 3 ],
               [ 4, 5 ],
               [ 6 ],
               [ 7, 8, 9, 10 ] ]

rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row]) # Now the number of cols depends on each row's length
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(ragged_list[row][col], " ", end="")
    print()
 """

    # List to be iterated through
values = [["a", "b", "c"],
          ["d", "e", "f"]]

    # "count" here is used to keep track of the index point
    # "value" is the value of the current element in the loop
    # The enumerate method take 2 arguements, the iterable and the starting
    # value for "count" which we set at 0 to represent the postion of the 
    # first index value in the list.

print("Below is the output generated:")
for row_idx, row in enumerate(values): 
    for col_idx, v in enumerate(row):
        print(f'Index ({row_idx},{col_idx}) contains the value {v}')