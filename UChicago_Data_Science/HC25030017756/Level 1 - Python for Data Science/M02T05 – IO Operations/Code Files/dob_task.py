# Read data from text file DOB.txt grabbing first two 
# entries as Name and last 3 as DOB
# Put data from each line into a string
# Print out two different sections - one for name and 
# One for birthdays



file_name = "/Users/harrycampbell/Documents/UChicago_Data_Science/HC25030017756/Level 1 - Python for Data Science/M02T05 – IO Operations/Code Files/DOB.txt"

# Create an empty string for the Names entries
names = ""

# Create an empty string for the DOB entries
birthdays = ""

# Open the file in read mode
with open(file_name, "r+") as file:
    for line in file:
        
        # Identify the first two spaces in each line
        first_space = line.find(" ")
        second_space = line.find(" ", first_space + 1)
        # Get up to the first two spaces into a string called names
        names = names + line[:(second_space)] + "\n"
        
        # Identify the last spaces in each line
        last_space = line.rfind(" ")
        second_last = line.rfind(" ", 0, last_space)
        third_last = line.rfind(" ", 0, second_last)
        # Get everything beyond the last three spaces into a string
        # called birthdays
        birthdays = birthdays + line[third_last + 1:]

# Print the lists separately
print("Name" + "\n" + names)
print("Birthdate" + "\n" + birthdays)