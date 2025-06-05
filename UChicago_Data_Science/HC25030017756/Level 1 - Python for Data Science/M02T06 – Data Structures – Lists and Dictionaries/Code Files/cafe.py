
import math

# Find the value of stock in the cafe you're running

# Create a list of items sold in the cafe
menu = ["coffee", "bagels", "tea", "donuts"]
inventory = [10, 6, 8, 12]
price = [4.99, 6, 2.99, 3.67]

# Create a dictionary that stores how many of each item is in inventory
stock = {menu[i]: inventory[i] for i in range(len(menu))}

# Create a dictionary that stores the price for each item in the menu
price = {menu[i]: price[i] for i in range(len(menu))}

# Calculate the total worth of the stock in the cafe 
total_stock = sum

item_value = {}
for item, num in stock.items():
    item_value[item] = num * price[item]
    total_stock = sum(item_value.values())

print(f"The total value of the cafe stock is ${total_stock}")





