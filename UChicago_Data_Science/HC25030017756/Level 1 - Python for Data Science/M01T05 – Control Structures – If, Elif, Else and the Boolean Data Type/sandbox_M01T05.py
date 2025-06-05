import os
os.system('cls' if os.name == 'nt' else 'clear')

""" 
# prompts the user to input a number between 1 and 100

num = int(input("Please input a number between 1 and 100: "))
 """
# Checks if the nuber is lower than 12, higher than 13 or exactly 13. 
# first if can be removed and output does not change based on elif blocks
""" 
if num < 12:
    print("The value you entered is lower than 12")
elif num > 13:
    print("The value you entered is higher than 13")
elif num < 13:
    print("The value ou entered is lower than 13")
else:
    print("The value you entered is 13")
 """
# !!!!!!! basic logic for if-elif-else blocks !!!!!! 
    
# FIRST Define your vairable(s)

# variabl_1 = ... # Replace '...' with your vairable
# variable_x = ... # Replace '...' with your variable
    
# THEN check your variable(s) against specific values
    
# if variable_1 ...: # Replace '...' with a comparison to a variable > < == ! 
    # What action should take place here? 
# elif variable_1 ...: # Replace '...' with a comparison to a variable
    # What should happen here if the first condition isn't met? 
# else: 
    # Finally, what should happen if none of the above conditions are met? 


"""!!!!!! 

# checks the current time and suggsts and activity
current_time = 11

if current_time < 11:
    print("Time for a short jog - let's go!")
elif current_time == 11:
    print("Only an hour left until lunch.")    
else: 
    print("It's after 11 - it's lunch time.") """

# Checks the current hour and sets a greeting based on the time of the day

""" 
hour = int(input("What time is it?: "))

if hour < 18:
    greeting = "Good day"
elif hour < 20:
    greeting = "Good evening"
else:
    greeting = "Good night"

print(greeting) """

date = int(input("What is today's date in April?: "))

if date < 14:
    reminder = ("No need to start packing yet")
elif date <= 17:
    reminder = ("You should probably start packing.")
elif date > 19:
    reminder = ("You totally missed moving day.")
elif date > 30:
    reminder = ("There aren't that many days in April.")
else:
    reminder = ("It would be crazy if you haven't started packing.")

print(reminder)