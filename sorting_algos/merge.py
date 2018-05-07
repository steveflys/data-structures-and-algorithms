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
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

    return my_list


"""This is a nonrecursive merge-sort with a Big O of 1 for space. 
I do not completly understand it, but I will at some point."""
# def merge_sort(my_list):
#     """Inplace merge sort of array without recursive. The basic idea
#     is to avoid the recursive call while using iterative solution. 
#     The algorithm first merges chunks of length of 2, then merges chunks
#     of length 4, then 8, 16"""
#
#     unit = 1
#     while unit <= len(my_list):
#         h = 0
#         for h in range(0, len(my_list), unit * 2):
#             l, r = h, min(len(my_list), h + 2 * unit)
#             mid = h + unit
#             # merge my_list[h:h + 2 * unit]
#             p, q = l, mid
#             while p < mid and q < r:
#                 if my_list[p] < my_list[q]: p += 1
#                 else:
#                     tmp = my_list[q]
#                     my_list[p + 1: q + 1] = my_list[p:q]
#                     my_list[p] = tmp
#                     p, mid, q = p + 1, mid + 1, q + 1

#         unit *= 2

#     return my_list
