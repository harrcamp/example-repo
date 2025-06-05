# triple quotes for 

long_string = ''' This is a long string
using triple quotes preserves everything inside is as a string even on a different line 
and with different \n spacing. '''

name = "Peter"
surname = "Parker"
age = 32
full_name = name + " " + surname

# cast other data types as strings to combine 
print(full_name + str(32))

# use format so it's not so clunky

sentence = "My name is {} and I'm {} years old.".format(name, age)
print(sentence)

# using f-string
sentence = f"My name is {name} and I'm {age} years old."
print(sentence)

# find length of a string
print(len("Hello, World!"))

# extract a chunk of a string
greeting = "abcdefg"
print(greeting[1:4])

# no ending index for the full length starting with first index
print(greeting[1:])

# negative numbers start from the ending index and go forward 
print(greeting[-3:])

# extended slide [begin : end : step] starts at the first parameter, ends at the second, and skips every third parameter arguement
print(greeting[1::2])

# reverse a string by adding a negative argument to the "skip" value of the extended string method
print(greeting[::-1])

# store a slice in a new variable
new_string = "Hello World!"
fizz = new_string[0:5]
print(fizz)
print(new_string)





