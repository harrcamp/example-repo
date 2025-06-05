import os
os.system('cls' if os.name == 'nt' else 'clear')

def add_three(num1, num2, num3):
    y = str(num1 + num2 + num3)
    return y

sum_func = add_three(num1=52, num2=25, num3=1403)

print(sum_func)







