
# gather input from user

#name
user_name = str(input("What is your name? "))

#age
user_age = int(input("How old are you?"))

# house number
user_house_number = str(input("What is your house number?"))

# Stree name
user_street_name = str(input("What street do you live on?"))

#test inputs
""" print(user_name)
print(user_age)
print(user_house_number)
print(user_street_name) """

# return phrase using fString method
""" print(f"This is {user_name}. They are {user_age} \
    years old and lives at house number {user_house_number} on {user_street_name}.") """

#  return phrase using indexes
print(
    "This is {0}. They are {1} years old and lives at house number {2} on {3}.".\
      format(user_name, user_age, user_house_number, user_street_name)) 

