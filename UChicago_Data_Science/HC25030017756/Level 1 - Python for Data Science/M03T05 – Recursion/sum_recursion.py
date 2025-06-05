def adding_up_to(integers, num):
    if num < 0 or num >= len(integers):
        raise IndexError
    
    # Base case: sum from the 0 index element
    if num == 0:
        return integers[0]
    
    # Recursive case: sum up to num-1, then add 
    return adding_up_to(integers, num - 1) + integers[num]

print(adding_up_to([1, 4, 5, 3, 12, 16], 4))
