import os
os.system('cls' if os.name == 'nt' else 'clear')
""" 
# initialise total sum to 0
total_sum = 0

# start with the first even integer
even_integer = 2

# Loop until the total sum exceeds 250
while total_sum <= 250:
    # Add the current even integer to the total sum
    total_sum += even_integer

    # Move to the next even integer
    even_integer += 2

    # Print the current total sum
    print(total_sum)


 """

""" # assignment statement control variable
i=0

# control with logical condition
while i < 10:

# input arguements
    i += 1 # shorthand for i = i + 1
    print(i)
 """

""" # Initialise the control variable to True
keep_running = True

# Start the loop
while keep_running:
    print("The loop is running.")
    # SEt the control variable to False to exit the loop
    keep_running = False
# ending result output
print("The loop has ended.")
 """
""" 
my_number = 0
# Loop until my_number is less than 100
while my_number < 100:
    my_number += 1

# if my_number equals 23, exit the loop
    if my_number == 23:
        break

 """

""" my_number = 0

# Loop until my_number is less than 100
while my_number < 100:
    my_number += 1

    # Skip further processing if my_number exceeds 23
    if my_number > 23:
        continue
    print(my_number)
 """

""" # initialise loop
for i in range (1,10):
    
    # loop test
    if i > 5:
        print(i)

 """
""" 
# Define a list of numbers
num_list = [1, 2, 3, 4, 5]

# Initialise a flag to indicate if the nyumber is found
found = False

# prompt the user to input a number from 1 to 10
num = int(input("Input a number from 1 to 10 and find out if it's in our list:"))

# Check if the input number is within the valid range
if num < 1 or num > 10:
    # Inform the user if the number is out of range
    print("Number out of range")
else:
    # Iterate through the list to check if the number is present
    for number in num_list:
        if num == number:
            # Set the flag to True if the number is found and exit the loop
            found = True
            break
    # Print the result indicating whether the number is in the list or not
    print(f'List contains {num}: {found}')
 """
# Outer loop, iterating over the range 1 to 5
for x in range(1, 6):
    # inner loop
    for y in range(1, 6):
        # print the multiplication result of x and y
        print(f"{x} * {y} = {x*y}")
    print("")


