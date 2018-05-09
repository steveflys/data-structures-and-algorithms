"""
Write a function that accepts an array of unsorted integers,
and returns a sorted array by a recursive quicksort algorithm.
"""


def quicksort(my_list):
    """Define a recursive quicksort function."""
    left = []
    pivot_list = []
    right = []
    if len(my_list) < 2:
        return my_list
    else:
        pivot = my_list[0]

        for item in my_list:
            if item < pivot:
                left.append(item)
            elif item > pivot:
                right.append(item)
            else:
                pivot_list.append(item)
        left = quicksort(left)
        right = quicksort(right)
        return left + pivot_list + right
