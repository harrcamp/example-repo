# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # defined key from for loop in function 

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", # added double quotes to match 
                                           # other entries in the dictionary
                         "maggie": "(Pacifier Suck)"
                         }

# Added parenthases to separate multiple keys in second function arguement in call
print_values_of(simpson_catch_phrases, ("lisa", "bart", "homer"))
                                                

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

