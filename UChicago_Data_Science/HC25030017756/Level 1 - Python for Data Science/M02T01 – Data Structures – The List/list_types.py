import os
os.system('cls' if os.name == 'nt' else 'clear')

# reminder slicing lists the 'end'arguement is not inluded in the slice

# .remove() = take out first occurance of a specific element in a list
# .pop() = remove and return the last element in a list
# del keyword to remove one or more items from the list

# create a list that stores three friend's names
friends_names = ["Cyrus", "Omar", "Harrison"]

# print first name in the list
print(friends_names[0])

# print last name in the list
print(friends_names[-1])

# print length of the list, or how many names are in the list
print(len(friends_names))


# define a list called 'friends ages'
friends_ages = [30, 29, 28]

# print each friend's name and age in separate sentences
for name, age in zip(friends_names, friends_ages):
    print(f"{name} is {age} years old.")