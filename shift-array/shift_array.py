def insert_shift_array(array, num):
    length = 0
    for n in array:
        length += 1
  
    # output_array = [0 for i in range(length + 1)]

    output_array = [0] * 5

    middle = (length + (length % 2)) / 2

    index = -1
    for i in output_array:
        index += 1
        if index < middle:
            output_array[index] = array[index]
        elif index == middle:
            output_array[index] = num
        else:
            output_array[index] = array[index - 1]
    return output_array


if __name__ == '__main__':

    insert_shift_array()
