# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


 # syntax error: missing parentheses
print("Welcome to the error program")

# syntax error: unexpected indent and syntax error missing parentheses
print("\n") 

<<<<<<< Updated upstream
"""  age_Str is declared with operator "==" or "is equal to". Changed to "=" which assigns variabls then cast age_Str to str (syntax), concatinated with the phrase and printed the result """
=======
"""  age_Str is declared with operator "==" or "is equal to". Changed to "=" which declares variabls then cast age_Str to str (syntax), concatinated with the phrase and printed the result """
>>>>>>> Stashed changes
age_Str = str(24)
age = int(age_Str)       
print("I'm " + age_Str + " years old.")

# Declare variables stating additional years and printing the total years of age
# syntax: unexpected indent for lines 14 - 15
# syntax: quotes removed from years_from_now as variables are automatically cast as int
<<<<<<< Updated upstream
# runtime: cast as integers to add like data types
years_from_now = 3                
total_years = str(age + years_from_now)  

# syntax: incorrectly defined varaible (answer_years)
=======
# syntax: cast as integers to add like data types
years_from_now = 3                
total_years = str(age + years_from_now)  

# syntax: misnamed varaible (answer_years)
>>>>>>> Stashed changes
# syntax: missing parenthases
# syntax: deleted quotes around variable in function, only strings require quotes
print("The total number of years: " + total_years)      
                                                       

# runtime: Variable to calculate the total number of months from the given number of years and printing the result
# logical: declared variable 'months' to add on 'total_years'
# syntax: replace total with total_years as a defined variable
<<<<<<< Updated upstream
# runtime: cast total_months as string becuase ints and strs can't concatonate
=======
# syntax: cast total_months as string becuase ints and strs can't concatonate
>>>>>>> Stashed changes
months = 6
total_months = int(total_years) * 12 + months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")      
 # syntax error missing parenthases

#HINT, 330 months is the correct answer
