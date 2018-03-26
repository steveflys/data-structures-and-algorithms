def largest_product(list):
    
    max = list[0][0] * list[0][1]

    outer_list = [1] * len(list)
    list_index = -1
    
    for i in outer_list:
        list_index += 1
        inner_list = [1] * len(list[list_index])
        inner_index = -1
        for j in inner_list:
            inner_index += 1
            if inner_index == len(inner_list) - 1:
                break
            product = list[list_index][inner_index] * list[list_index][inner_index + 1]
            if max < product:
                max = product  
    return max            

if __name__ == '__main__':
    largest_product([[1,2], [2,3], [3,4], [1, 5, 4, 6]])