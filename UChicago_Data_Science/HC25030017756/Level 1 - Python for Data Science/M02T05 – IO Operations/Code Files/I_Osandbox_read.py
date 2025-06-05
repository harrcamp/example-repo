file = open('example.txt', '+r')
# operations on the open file go here
file.close()

# context manager can also be used 'with' and 'as'
# closes files automatically when operations are complete

# with open('example.txt', 'r+') as file:
    # perform file operations on the open file
    # the code must be indented to be part of the 'with' block. 

with open("example.txt", "r+") as file:
    # 'lines' will contain a string with all the data from the file. 
    lines = file.read()    # Reads all data from the file. 

with open("example.txt", "r+") as file:
    lines = file.read(10)    # Reads 10 characters from the file

with open("example.txt", "r+") as file:
    line = file.readline() # reads a single line from the file

with open("example.txt", "r+") as file:
    # 'lines' contains each line of the text file as a list element. 
    lines = file.readlines() # reads each line of data in the file

# looping through the file
with open("example.txt", "r+") as file:
    for line in file:
        # reads each line of data in the file
        print(line) # Desplays each line within 'example.txt". 


with open("example.txt", "r+") as file:
    # Iterate through each line in the file
    for line in file:
        # Print the entire line
        print("The entire line is: " + line)

        # print the first character of the line
        print("The first character of this line is: " + line[0])

# build up all the lines of the text file into one large string:  
contents = "" # Initiates an empty string to store the contents

with open("example.txt", "r+") as file:
    # Open the file and iterate through each line
    for line in file:
        contents = contents + line # Append each line to 'contents'

# Print the contents outside the 'with' statement
print(contents)



lines = [] # initialise an empty list to store each line

with open("example.txt", "r+") as file:
    # Open the file and iterate through each line
    for line in file:
        lines.append(line)  # Append each line to the 'lines' list

# Print the lines stored in the list
print(lines)

