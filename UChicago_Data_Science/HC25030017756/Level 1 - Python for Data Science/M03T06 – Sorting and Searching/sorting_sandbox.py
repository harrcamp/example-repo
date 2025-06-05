""" from queue import Queue

# Creating new Queue
students = Queue()

# Adding studnt to the queue wit put
students.put("Kylie")
students.put("Julia")
students.put("Glitch")

# Iterate over all students with a While loop where 'empty'
# returns False when items are in the queue. If NOT empty THEN full 
# THEREFORE get next in queue
while not students.empty():
    # Get curent student and remove from queue until empty() returns True
    # i.e. get students out of the queue until the queue is empty
    current_student = students.get()
    print(current_student)


#___________!!!!!!__________#
    
# A list can also be used as a stack
my_pets = []

# Add 3 entries to the stack
my_pets.append("Dog")
my_pets.append("Cat")
my_pets.append("Ferret")
print(my_pets)

# Pop out Ferret from the list becuase it was the Last Entered
my_pets.pop()
print(my_pets) """

#__________!!!!!!__________#

""" def bubble_sort(items):
    # Traverse through all elements in the list
    for i in range(len(items) - 1, -1, -1):
        # Traverse the list from 1 to i
        for j in range(1, i + 1):
            # Swap if the element is greater than the next element
            if items[j - 1] > items[j]:
                items[j - 1], items[j] = items[j], items[j - 1]
    return items

# Usage
example_list = [1, 3, 2, 6, 7, 4, 11, 5]
sorted_list = bubble_sort(example_list)
print(sorted_list)
 """
#_________##_________!!

""" def quick_sort(items, low, high):
    if low < high:
        # Partition the list and get the pivot index
        mid = partition(items, low, high)

        # Recursively sort the lef partition
        items = quick_sort(items, low, mid - 1)

        # Recursively sort the right partition
        items = quick_sort(items, mid + 1, high)

    return items

def partition(items, low, high):
    # The pivot point is the first item in the sublist
    pivot = items[low]

    # Loop through the list. Move items up or down the list so that they 
    # are in the proper spot with regards to the pivot point
    while low < high:
        # Can we find a number smaller thanthe pivot point:
        # Keep moving the high marker dow the list until we find this
        # or until high == low
        while low < high and items[high] >= pivot:
            high -= 1

        if low < high:
            # found a smaller number, swap it into position
            items[low] = items[high]
            # Now look for a number larger than the pivot point
            while low < high and items[low] <= pivot:
                low += 1

            if low < high:
                # Found one! Move it into position
                items[high] = items[low]

    # Move the pivot back into the list and return its index
    items[low] = pivot
    return low

# Example usage:
example_list = [33, 10, 59, 26, 41, 58, 18]
sorted_list = quick_sort(example_list, 0, len(example_list) - 1)
print(sorted_list) """


###____!!!!____!!!!____###

def merge_sort(items):
    # Get the lengh of the input list
    items_length = len(items)

    # Create temporary storage for merging
    temporary_storage = [None] * items_length

    # Initialize the size of subsections to 1
    size_of_subsections = 1

    # Iterate until the size of subsections is less than the length of the list
    while size_of_subsections < items_length:
        # Iterate over the list in steps of size_of_subsections * 2
        for i in range(0, items_length, size_of_subsections * 2):
            # Determine the start and end indices of the two subsections
            # to merge.
            first_section_start, first_section_end = i, min(
                i + size_of_subsections, items_length
            )
            second_section_start, second_section_end = first_section_end, min(first_section_end + size_of_subsections, items_length
            )

            # Define the sections to merge
            sections = (first_section_start, first_section_end), (
                second_section_start,
                second_section_end,
            )

            # CAll the merge function to merge the subsections
            merge(items, sections, temporary_storage)

        # Double the size of subsections for the next iteration
        size_of_subsections *= 2

    return items

def merge(items, sections, temporary_storage):
    # Unpack the sections tuple to get the start and end indices
    # of each section.
    (first_section_start, first_section_end), (
        second_section_start, 
        second_section_end,
    ) = sections

    # Initialise indices for the two sections and temporary storage
    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    # Loop until both sections have been fully merged
    while left_index < first_section_end or right_index < second_section_end:
        # Check if both sections still have elements to compare
        if left_index < first_section_end and right_index < second_section_end:
            # Compare elements from both sections
            if items[left_index] < items[right_index]:
                # Place the smaller element into temporary storage
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
            else:   # items[right_index <= items[left_index]
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
            temp_index += 1

        # If section 1 stil has elements left to merge
        elif left_index < first_section_end:
            # Copy remaining elements from section 1 to temporary storage
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        # If section 2 still has elements left to merge
        else: # right_index < section_section_end
            # Copy remaining elements from section 2 to temporary storage
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1
        # Copy sorted elements from temporary storae back to the original list
        for i in range(temp_index):
            items[first_section_start + i] = temporary_storage[i]

# Example usage:
example_list = [33, 10, 59, 26, 41, 58, 18]
sorted_list = merge_sort(example_list)
print(sorted_list)