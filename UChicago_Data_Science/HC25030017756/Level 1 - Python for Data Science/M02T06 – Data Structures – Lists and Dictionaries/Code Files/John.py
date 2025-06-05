# Request the user to enter the value "John" into the input box
# Add all entries to a list until John is entered
# print the list of incorrectly entered names
input_name = ""

# Initiate an empty list to store the inputs
names = []

while True:
    # Request user to input a name
    input_name = str.lower(input("Enter your name: "))

    # If input is not John, add the name to names and prompt the user 
    if input_name != "john":
        names.append(input_name)
        continue

    # Check if the input is "John", if so break the loop
    if input_name == "john":
        if names == []:
            print("No other names were entered.")
        else:
            capitalized_names = [input_name.capitalize() for input_name in names]
            print(f"Incorrect names: {capitalized_names}")
        break
 