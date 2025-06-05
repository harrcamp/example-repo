import os
os.system('cls' if os.name == 'nt' else 'clear')

# variety of responses based on user age input

age = int(input("How old are you?: "))

# check if the age is 100 or over
if age >= 100:
    age_response = ("Sorry, you're dead.")

# check if age is between 99 and 65
elif age >= 65:
    age_response = ("Enjoy your retirement!")

# check if age is between 64 and 40
elif age >= 40:
    age_response = ("You're over the hill.")

# check if age is exactly 21
elif age == 21:
    age_response = ("Congrats on your 21st!")

# check if age is under 13
elif age < 13:
    age_response = ("You qualify for the kiddie discount!")

# if none of the above conditions are met, output a default message
else:
    age_response = ("Age is but a number.")

print(age_response)

# function then checks for maximum to output the reponse and then downward