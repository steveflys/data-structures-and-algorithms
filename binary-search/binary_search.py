
def binary_search(list, number):
    min = 0

    max = len(list) - 1

    while min != max:

        center = new_center

        if list[center] = number:
            return center

        elif list[center] > number:
            new_center(center, max)
        
        else:
            new_center(min, center)


def new_center(max, min):
    return (max - min)/2 + min







if __name__ == '__main__':