def cut_cake(number_of_friends, number_of_slices):
    # Cut cake in half
    number_of_slices = number_of_slices * 2

    # Check if there are enough slices for everybody
    if number_of_slices >= number_of_friends: # Base case
        # If there are enough slices - return the number of slices
        return number_of_slices
    
    else:
        # If there are not enough slices - cut the resulting
        # slices in half again
        return cut_cake(number_of_friends, number_of_slices)
    
print(cut_cake(11, 1))

#_______________!!!!!!!_________________#

def factorial(n):
    # Base case: if n is 0, return 1 becuase 0! is defined as 1
    if n == 0:
        return 1
    else:
        # Recursive case: calculate n! by multiplying n with the factorial
        # of (n - 1)
        return n * factorial(n - 1)
    
print(f"The factorial of 4 is {factorial(4)}")
