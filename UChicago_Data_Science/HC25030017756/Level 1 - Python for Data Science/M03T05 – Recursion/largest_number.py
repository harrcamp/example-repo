def largest_number(lst):
    """
    Recursively find the largest number in a non-empty list of integers.
    
    Args:
        lst (list of int): The list to search; must contain at least one element.
        
    Returns:
        int: The largest integer in the list.
        
    Raises:
        ValueError: If lst is empty.
    """
    if not lst:
        raise ValueError("largest_number() requires at least one element")
    
    # Base case: a single-element list
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: compare first element to the largest of the rest
    head = lst[0]
    max_of_rest = largest_number(lst[1:])
    return head if head > max_of_rest else max_of_rest


print(largest_number([1, 4, 5, 3])) 