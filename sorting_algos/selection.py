# """Do a selection sort of a list of elements"""


# def selection_sort(list):
#     """Define the selection sort algorithm"""
#     i = 0
#     for i in range(0, len(list)-1, +1):
#         smallest = list[i]
#         while i < len(list):
#         i += 1
#         if list[i] > smallest:
#             smallest = list[i]


# def selectionSort(alist):
#     for fillslot in range(len(alist)-1, 0, -1):
#         positionOfMax = 0
#         for location in range(1, fillslot+1):
#             if alist[location]>alist[positionOfMax]:
#                 positionOfMax = location

#         temp = alist[fillslot]
#         alist[fillslot] = alist[positionOfMax]
#         alist[positionOfMax] = temp

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# selectionSort(alist)
# print(alist)
