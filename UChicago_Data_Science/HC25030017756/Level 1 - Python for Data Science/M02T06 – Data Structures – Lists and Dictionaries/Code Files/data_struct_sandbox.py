import copy

a = [[1, 2, 3], [4, 5, 6]] # original list
b = a[:] # copy of first list using slice
c = copy.deepcopy(a) # copy of first list using copy() method. 
                     # No changes from b
b[0][2] = 10 
c[1][1] = 12
print(a)
print(b)
print(c)

food_list = ["Pizza", "Burger", "Fries", "Pasta", "Salad"]

# food represents the strings in food_list and therefore contain the method upper()
food_list_upper = [food.upper() for food in food_list]
print(food_list_upper)
i=0

# using a while loop
while i < len(food_list):
    # Print the element at that position
    print(food_list[i])
    # Increment i
    i+=1

# using a for loop
for food in food_list:
    print(food)

num_list = ['1', '5', '8', '14', '25', '31']
new_num_list_ints = [int(element) for element in num_list]
by_two_num_list = [(int(element) * 2) for element in num_list]

print(new_num_list_ints)
print(by_two_num_list) 

# create a dictionary 
int_key_dict = {1: 'apple',
                2: 'banana',
                3: 'orange'
                }

int_key_list = [(1, 'apple'), (2, 'banana'), (3, 'orange')]
int_key_dict = dict(int_key_list)
print(int_key_dict)

# set the tuple similar to a variable
my_tuple = (1, 'apple')

# call the tuple, first is xyz in my_tuple second is value in my_tuple. Setting variables to tuple
xyz, value = my_tuple

print(xyz)

# accessing elements from a dictionary
print(int_key_dict[1]) # prints out apple
print(int_key_dict.get(2))

# print keys and values
keys_fruit = int_key_dict.keys()
values_fruit = int_key_dict.values()

print(keys_fruit)
print(values_fruit)

# changing elements in a dictionary
int_key_dict[1] = 'grapes'
print(int_key_dict)

int_key_dict[4] = 'pineapple'
print(int_key_dict)

# test for values in a dictionary
print(1 in int_key_dict)