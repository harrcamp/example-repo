# check if a file exists

""" import os
import time

print(os.path.exists("output.txt"))     # Returns True if the file exists

print(os.path.getsize("output.txt"))    # Returns the size of the file in bytes

# Get the last modification time of the file
last_modified = os.path.getmtime('output.txt')

# Convert the time to a human-readable format
last_modified_str = time.ctime(last_modified)

# Print the last modification time
print(last_modified_str) """

name = input("Enter name: ")

with open("output.txt", "w") as f:
    f.write(name + "\n")

# Very Important: file exception handling

try:
    # Attempt to open 'example.txt' in read mode
    with open("output.txt", "r+") as file:
        # Read the entire content of the file into "content
        content = file.read()

    # Print the content of the file
    print(content)

except FileNotFoundError:
    # Handle the case where 'output.txt' does not exist
    print("The file does not exist. Please check the file path and try again.")