import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

# request from the user whether they are interested in calculating the interest they will earn on an investment or 
# how much they will have to pay for a home loan

print("Investment - to calculate the amount of interest you'll earn on  your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")
print("\n")

# Store the input answer in a variable called calculation_type
calculation_type = str.lower(input('Enther either "investment" or "bond" from the menu above to proceed: '))                      

# confirm selection of 'investment' by repeating user input
# for clarity
if calculation_type == "investment":
    print(f"You have selected {calculation_type} calculation.")
    print()

    # request inputs for principal (starting balance), 
    # interest rate (rate which principal is multiplied), 
    # interest period (for how long interest will accrue), 
    # and periodicity of calculation (simple or compound)
    principal  = float(input("How much money are you investing?: "))
    interest_rate_inv = (float(input("What is the interest rate? (only enter a number): ")) / 100)
    interest_period = float(input("For how many years are you investing?: "))
    interest_type = str.lower(input("Would you like simple or compound interest?: "))   
 
    # Exit if an invalid interest type is entered by the user
    if interest_type not in ("simple", "compound"):
        print("Please only enter either 'simple' or 'compound'")
        exit()
 
    # multiply the principal investment by 100+X (to represent 
    # growth rate then by the number of periods
    if interest_type == ("simple"):
        total_investment = principal * (1 + interest_rate_inv * interest_period)
        print()
        print(f"After {math.trunc(interest_period)} years your investment will be worth ${round(total_investment, 2)}")

    # multiply the principal investment by 100+X^(number of periods)
    # to represent continuously multiplicative values over a period 
    # of time
    elif interest_type == ("compound"):
        total_investment = principal * math.pow((1 + interest_rate_inv), interest_period)
        print()
        print(f"After {math.trunc(interest_period)} years your investment will be worth ${round(total_investment, 2)}")
        print("Look at the power of compound interest!")

# confirm selection of 'bond' by repeating user input for clarity
if  calculation_type == "bond":
    print(f"You have selected {calculation_type} calculation.")
    print()

    # request numerical inputs for base loan amount (present value), 
    # interest rate (the cost to borrow money), and number of payment
    # periods
    present_value = float(input("What is the present value of the house?: "))
    interest_rate_b = ((float(input("What is the interest rate for the loan? (annual): ")) / 12) / 100)
    payment_period = float(input("Over how many months do you plan to repay the bond?: "))

    # using the standard amortisation formula, calculate monthly
    # repayment amount
    repayment = interest_rate_b * present_value / (1 - (1 + interest_rate_b) ** (-payment_period))
    print()
    print(f"Your monthly repayment amount is ${round(repayment, 2)}")

# check first for valid user input of calculation selection
# exit if input is not 'investment' or 'bond'
elif calculation_type != "investment" and calculation_type != "bond":
    print("Please only enter either 'investment' or 'bond'.")
