# 1. LINEAR SEARCH (for unsorted lists)
def linear_search(arr, target):
    """
    Scans each element until it finds target.
    Good choice here because the list is unsorted
    and linear search runs in O(n) without preprocessing.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # not found

data = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
idx = linear_search(data, 9)
print(f"Linear search: 9 found at index {idx}")

#____!!!!____#

# 2. INSERTION SORT
def insertion_sort(arr):
    """
    Builds a sorted array one element at a time,
    inserting each new element into its proper place.
    Runs in O(n^2) worst-case, but is simple and in-place.
    """
    a = arr[:]  # make a copy so we don't overwrite original
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # Shift larger elements rightward
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

sorted_data = insertion_sort(data)
print("Sorted list:", sorted_data)

#____!!!!____#

# 3. BINARY SEARCH (on sorted lists)
def binary_search(arr, target):
    """
    Fast O(log n) lookup by halving the search interval each time.
    You'd use this in any system requiring quick lookups over sorted data:
    e.g. database indexes, dictionary word lookups, log file timestamp search, etc.
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1  # not found

idx2 = binary_search(sorted_data, 9)
print(f"Binary search: 9 found at index {idx2} in the sorted list")

