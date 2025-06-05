# Define data file for calculation input
file_path = "/Users/harrycampbell/Documents/UChicago_Data_Science/HC25030017756/Level 1 - Python for Data Science/M03T01 – Defensive Programming – Exception Handling/equations.txt"

# Define a function calculation
def calculation(first, operand, second):
    """
    Takes user input for a basic math equation
    then calculates the answer, printing the result and recording in a text file for recall at-will.

    Args: 
    (int) first value, (str) operand, (int) second value

    Returns:
    (str) answer to the calculation
    """
    if operand == "/":
        calc = first / second
    elif operand == "*":
        calc = first * second
    elif operand == "+":
        calc = first + second
    elif operand == "-":
        calc = first - second
    else:
        raise ValueError("Not a valid operand.")
    return calc

# Create an options list for the user to either enter a 
# New calculation or view the list of calculations already
# Processed

def options():
    """
    Print the available options for the user.
    """
    print("Options: \n")
    print("c = enter values to perform basic math.")
    print("p = display previously entered calculations.")
    print("q = quit")


# Set choice to random value excluded from list
choice = "x"

# Request calculations or print values until the user chooses to quit
while choice != "q":
    # Display the options avilable to the user
    options()

    choice = input("Please enter your choice: ")
    if choice == "c":
        # Request user input for numbers in the calculation then store in separate variables to pass as arguements in calculation function call
        
        # Loop until an integer is entered for the first value
        while True:
            try:
                first = int(input("Enter the first value in the calculation: "))
                break
            except ValueError:
                print("Not an integer, try again")
        valid_ops = {"+", "-", "*", "/"}
        while True:
            operand = input("Enter the operation (+, -, *, /)")
            if operand in valid_ops:
                break
            print("Invalid operand. Please use '+', '-', '*', '/'")        
        # Loop until an integer is entered for second values
        while True:
            try:
                second = int(input("Enter the second value in the calculation: "))
                if operand == "/" and second == 0:
                    print("Cannot divide by zero. Please enter a non-zero integer.")
                    continue
                break
            except ValueError:
                print("Not an integer please try again.")
        # Perform the calculation from user input and print the whole operation
        calc = (calculation(first, operand, second))
        print(f"Answer: {calc}")
        # Write the operation in the file 
        with open(file_path, "a+") as f:
            f.write(f"{first} {operand} {second} = {calc}\n")
    elif choice == "p":   
        # User chooses to print previously entered equations:
        def print_equations(content):
                # File exception handling. Check if the file exists or not in he path
            try:
                # Attempt to open 'equations.txt' in read mode
                with open(file_path, "r+") as file:
                    # Read the entire content of the file into "content
                    content = file.read()
                # Print the content of the file
                print(content)
            except FileNotFoundError:
                # Handle the case where 'output.txt' does not exist
                print("The file does not exist. Please check the file path and try again.")
        print_equations(file_path)  
    elif choice == "q":
        # Quit the program
        print("")
    else:
        # Handle unrecognized input
        print("Unrecognized option.")