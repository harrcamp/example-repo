
import statistics
import math

# Initiate an empty list to store user inputs
floats = []
entry_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Requets 10 floats from the user and store in list Floats
for num in range(10):
    input_floats = float(input("Please input 10 numbers, some including decimals: "))
    floats.append(input_floats)

# Calculate the total of entries by the user
floats_total = sum(floats)
print(f"The sum total of user entries is: {floats_total}")

# Identify the maximum value among user entries and its index value
floats_max = floats.index(max(floats))
print(f"The index of the max number entered by the user is: {floats_max}")

# Identify the minimum value among user entries and its index value
floats_min = floats.index(min(floats))
print(f"The index value of the min number entered by the user is: {floats_min}")

floats_mean = round(sum(floats) / (len(floats)), 2)
print(f"The mean of the numbers rounded to 2 decimal places is: {floats_mean}")

floats_median = statistics.median_high(floats)
print(f"The median value (rounded up) of user input values is: {floats_median}")