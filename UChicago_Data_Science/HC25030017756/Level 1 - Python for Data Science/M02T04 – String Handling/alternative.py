""" import os
os.system('cls' if os.name == 'nt' else 'clear')

# prompt the user to input a string of characters 
input_string = str(input("Please input a sentence or string of words: "))

# pull every other character to substring 1
new_string_1 = (input_string[::2]).upper()

# pull second character every other into substring 2
new_string_2 = (input_string[1::2]).lower()

max_length = max(len(new_string_1), len(new_string_2))

combined = []

for i in range(max_length):
    if i < len(new_string_1):
        combined.append(new_string_1[i])
    if i < len(new_string_2):
        combined.append(new_string_2[i])
        
result = ''.join(combined)
print(result) """

# __________________!!!!!!!!!!!!!!!!!!!!!____________________ #

# prompt the user to input a string of characters 
input_string = str(input("Please input a sentence or string of words: "))

# break the string up into words in a list
split_string = input_string.split()

# create a new empty list for the words to be put into
combined_list = []

# loop through even indices to make lower case and odd indices upper case
for num in range(len(split_string)):
    if num % 2 == 0:
        # split_string[index] represents a string. Must pass an index for the list to call a string to the method
        combined_list.append(split_string[num].lower())
    else:
        combined_list.append(split_string[num].upper())
   
# join  the restulting strings
result = ' '.join(combined_list)
print(result)

