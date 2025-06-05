
# Import the Random functoin
import random

# Create a program that generates random jokes 

# Fill a list with jokes and punchlines
jokes_list = [
    "Why did the math book look sad? \nBecause it had too many problems.",
    "Why did the scarecrow win an award? \nBecause he was outstanding in his field.",
    "Why don’t eggs tell jokes? \nThey’d crack each other up.",
    "What do you call a bear with no teeth? \nA gummy bear.",
    "Why did the bicycle fall over? \nBecause it was two-tired."
]

# Initiate a list for dict keys to assign to jokes
jokes_key = [1, 2, 3, 4, 5]

# Create a dictionary with the key and joke pairs
jokes_dict = dict(zip(jokes_key, jokes_list))

# Assign a random key to the variable 'random_joke'
random_joke = random.choice(range(len(jokes_dict)))

# Get the joke paired with the key from 'jokes_list' 
print(jokes_list[random_joke])