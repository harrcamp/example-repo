import copy

# Modified merge sort to sort strings by length from longest to shortest
def merge_sort(items):
    items_length = len(items)
    temporary_storage = [None] * items_length
    size = 1
    while size < items_length:
        for i in range(0, items_length, 2 * size):
            first_start = i
            first_end = min(i + size, items_length)
            second_start = first_end
            second_end = min(first_end + size, items_length)
            merge(items, first_start, first_end, second_start, second_end, temporary_storage)
        size *= 2
    return items

def merge(items, fs, fe, ss, se, temp):
    li, ri, ti = fs, ss, 0
    # Merge by comparing lengths (longest first)
    while li < fe and ri < se:
        if len(items[li]) > len(items[ri]):
            temp[ti] = items[li]
            li += 1
        else:
            temp[ti] = items[ri]
            ri += 1
        ti += 1
    # Copy any remaining elements
    while li < fe:
        temp[ti] = items[li]
        li += 1; ti += 1
    while ri < se:
        temp[ti] = items[ri]
        ri += 1; ti += 1
    # Write back to original list
    for j in range(ti):
        items[fs + j] = temp[j]

# Three example lists (unsorted, at least 10 elements each)
list1 = ["elephant", "dog", "hippopotamus", "cat", "giraffe", "ant", "rhinoceros", "mouse", "crocodile", "bee", "alligator", "fox"]
list2 = ["blue", "indigo", "violet", "red", "turquoise", "brown", "black", "yellow", "magenta", "pink", "orange", "gray"]
list3 = ["ChatGPT", "OpenAI", "Artificial Intelligence", "AI", "Machine Learning", "Deep Learning", "Neural Network", "Data Science", "Natural Language Processing", "Reinforcement Learning"]

# Run and display results
for idx, lst in enumerate([list1, list2, list3], start=1):
    original = copy.deepcopy(lst)
    sorted_lst = merge_sort(lst)
    print(f"List {idx} - Original:\n{original}\nList {idx} - Sorted by length (longest→shortest):\n{sorted_lst}\n")

