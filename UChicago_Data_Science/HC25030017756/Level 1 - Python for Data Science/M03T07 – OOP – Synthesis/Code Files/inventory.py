"""
shoe_inventory.py

A tool to manage a shoe inventory.
This program reads and writes data from a text file.
Users can view, search, and update items as needed.
"""

# Define path to inventory file relative to this script
FILE_PATH = "inventory.txt"

# Global list to store Shoe objects in memory
shoes_list = []



class Shoe:
    """
    Represents a shoe with country, code, product, cost, and quantity.

    Attributes:
        country (str): Warehouse location of Shoe.
        code (str): Inventory SKU code.
        product (str): Name of the shoe model.
        cost (float): Cost price per unit.
        quantity (int): Units available in stock.

     Methods:
        __init__(country, code, product, cost, quantity):
            Initializes a new Shoe instance.

        get_cost():
            Return the cost of the shoes.
        
        get_quantity():
            Return the quantity left in inventory for a shoe. 
    """
    def __init__(self, country, code, product, cost, quantity):
        # Initialize attributes with type conversion and error handling
        self.country = country
        self.code = code
        self.product = product
        try:
            self.cost = float(cost)
        except ValueError:
            self.cost = 0.0
        try:
            self.quantity = int(quantity)
        except ValueError:
            self.quantity = 0

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):  # noqa: D105
        # Provide readable string representation for printing
        return (
            f"Country: {self.country} | Code: {self.code} | "
            f"Product: {self.product} | Cost: {self.cost} | "
            f"Quantity: {self.quantity}"
        )



# Function to read data from inventory file into shoes_list

def read_shoes_data(filename=FILE_PATH):
    """
    Read shoe data from file and populate the shoes_list.
    Skip header and handle missing file or malformed lines.
    """
    # Clear existing list to prevent duplicate entries
    shoes_list.clear()
    try:
        with open(filename, "r") as file:
            next(file)  # Skip header line
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 5:
                    continue
                country, code, product, cost, qty = parts
                shoe = Shoe(country, code, product, cost, qty)
                shoes_list.append(shoe)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as err:
        print(f"Error reading data: {err}")


# Function to prompt user for new shoe info and add to list

def capture_shoes():
    """
    Prompt user to enter shoe details and add to inventory list.
    Data will not be saved to file until update_file is called.
    """
    country = input("Enter country: ")
    code = input("Enter SKU code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe added to inventory.")


# Function to display all shoes currently stored in memory

def view_all():
    """
    Print all shoes in the inventory list or a message if empty.
    """
    if not shoes_list:
        print('No shoes in inventory.')
        return
    print('\nCurrent Inventory:')
    for shoe in shoes_list:
        print(shoe)


# Function to overwrite inventory file with current shoes_list data

def update_file(filename=FILE_PATH):
    """
    Write the global shoes_list back to the inventory file.
    Rewrites header and each Shoe as a CSV line.
    """
    try:
        with open(filename, "w") as file:
            file.write('Country,Code,Product,Cost,Quantity\n')
            for shoe in shoes_list:
                line = (
                    f"{shoe.country},{shoe.code},"
                    f"{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
                file.write(line)
    except Exception as err:
        print(f"Error writing file: {err}")


# Function to find and optionally restock lowest-quantity shoe

def re_stock():
    """
    Identify shoe with lowest quantity and prompt to restock.
    Update file if user confirms addition.
    """
    if not shoes_list:
        print('No shoes in inventory.')
        return
    lowest = min(shoes_list, key=lambda s: s.quantity)
    print('\nLowest quantity item:')
    print(lowest)
    choice = input('Restock this item? (yes/no): ').strip().lower()
    if choice == 'yes':
        try:
            add_qty = int(input('Enter quantity to add: '))
            lowest.quantity += add_qty
            update_file()
            print('Inventory updated.')
        except ValueError:
            print('Invalid number entered.')
    else:
        print('No changes made.')


# Function to search for a shoe by its SKU code

def search_shoe():
    """
    Prompt user for SKU code and display matching shoe.
    Return Shoe object if found, else None.
    """
    code = input('Enter SKU code to search: ').strip()
    for shoe in shoes_list:
        if shoe.code == code:
            print('\nShoe found:')
            print(shoe)
            return shoe
    print('Shoe not found.')
    return None


# Function to calculate and display total value per item

def value_per_item():
    """
    Calculate total value (cost * quantity) for each shoe.
    Print product name, code, and computed total value.
    """
    if not shoes_list:
        print('No shoes in inventory.')
        return
    print('\nValue per item:')
    for shoe in shoes_list:
        total = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} ({shoe.code}): {total}")


# Function to identify and display shoe for sale (highest quantity)

def highest_qty():
    """
    Determine shoe with the highest quantity and mark for sale.
    Display the Shoe object details to the user.
    """
    if not shoes_list:
        print('No shoes in inventory.')
        return
    top = max(shoes_list, key=lambda s: s.quantity)
    print('\nItem with highest quantity (FOR SALE):')
    print(top)


# Function to display menu and respond to user choices iteratively

def menu():
    """
    Main menu loop for user interaction with inventory tool.
    Calls other functions based on user selection.
    """
    read_shoes_data()
    while True:
        print('\nMenu:')
        print('1. View all shoes')
        print('2. Capture new shoe')
        print('3. Restock lowest quantity item')
        print('4. Search shoe by code')
        print('5. Calculate value per item')
        print('6. Show item for sale (highest quantity)')
        print('7. Exit')
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')


# Entry point for script execution when run directly

if __name__ == '__main__':
    menu()
