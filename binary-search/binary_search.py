
def binary_search(list, number):
    min = 0

    max = len(list) - 1

    num = int(number)

    last_center = 0 

    while min != max:

        center = new_center(min, max)  

        if list[center] == num:
            return center
        elif last_center == center:
            return - 1    
        elif last_center == (center - 1):
            return - 1
        elif last_center == (center + 1):
            return -1 
        elif list[center] < num:
            new_center(center, max)
            last_center = center
        else:
            new_center(min, center)
            last_center = center



def new_center(max, min):
    print(int((max - min)/2 + min))
    return int((max - min)/2 + min)


if __name__ == '__main__':
    binary_search()