
# user enters a sentence
str_manip = input("Please input a sentence: ")

# display the length of input
str_len = len(str_manip)
print(f"The length of your string is: {str_len}")

# Replace 
str_last = str_manip.replace(str_manip[-1:], "@")
print(f"Sentence after replacing '{str_manip}' with '@': {str_last}")

str_back = str_manip[::-1][:3]

""" str_back_last = str_back[:3] !!!! The code above 
is more efficient than passing 
through multiple functions storing two vairables """

print(str_back) 

# Return a five-letter word that is made up of the first 
# three characters and th elast two chracter in str_manip

str_first_three = (f"{str_manip[:3]}" + f"{str_manip[-2::1]}")
print(str_first_three)

