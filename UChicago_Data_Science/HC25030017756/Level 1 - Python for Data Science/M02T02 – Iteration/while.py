import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

""" # set the control variable to 1
i = 1

# create empty list to put user inputs in
num_list = []

# if the number = -1 then exit the loop
while i != -1:

    # ask the user to enter a number and add it to the list
    i = int(input("Please enter a number: "))
    num_list.append(i)
    
    # if 0 is entered it could return a 'divide by 0' error
    # therefore 0 is not a valid input delete it from the list
    while i == 0:
        print("0 is not a valid input. Please enter a different number.")
        del num_list[-1:]
        break
    
    # remove -1 from the list and stop the loop to only calculate valid
    # entries
    if i == -1:
        del num_list[-1:]

# return the average of the numbers entered by the user excluding 0
# and -1 
print(f"The average of the list is {sum(num_list)/(len(num_list))}")
print(f"the list is {len(num_list)} entries long")
print(f"the sum of the list is {sum(num_list)}")
print(num_list) """

# model answer

# Initialise variables to store the sum and count of numbers entered
total = 0
count = 0


# Continuously ask the user to enter a number
while True:
    # Get user input
    num = input("Enter a number (enter -1 to stop): ")


    # Check if the input is '-1', if so, break out of the loop
    if num == '-1':
        break


    # Check if the input consists of digits (positive or negative integer)
    if not num.lstrip('-').isdigit():
        print("Invalid input! Please enter a real number.")
        continue


    # Convert the input to a float
    num = float(num)


    # Increment the count and add the number to the total
    count += 1
    total += num


# Check if any numbers were entered (excluding -1)
if count > 0:
    # Calculate the average
    average = total / count
    print(f"The average of the numbers entered is: {average}")
else:
    print("No numbers entered.")
