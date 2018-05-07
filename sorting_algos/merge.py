"""Define the Merge Sort function."""


def merge_sort(my_list):
    """Make a merge sort on an list."""
    if len(my_list) < 1:
        return my_list
    if len(my_list) > 1:
        middle = len(my_list) // 2
        left_half = my_list[:middle]
        right_half = my_list[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        # print('\nno_while_comp:', my_list)
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        # print('\nfirst_while_comp:', my_list)
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        # print('\nsecond_while_comp:', my_list)
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1
        # print('\nthird_while_comp:', my_list)
    return my_list
