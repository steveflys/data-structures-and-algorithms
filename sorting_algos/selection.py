"""Do a selection sort of a list of elements."""


def selection_sort(my_list):
    """Define the selection sort algorithm."""
    if len(my_list) < 1:
        return my_list
    for index in range(0, len(my_list)-1, +1):
        index_of_min = index
        for location in range(index, len(my_list)):
            if my_list[location] < my_list[index_of_min]:
                index_of_min = location

        temp = my_list[index]
        my_list[index] = my_list[index_of_min]
        my_list[index_of_min] = temp

    return my_list
