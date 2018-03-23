def largest_product(list):
    
    max = list[0][0] * list[0][1]

    for i in list -1:
        for j in list[i] - 2:
            product = list[i][j] * list[i][j + 1]
            if max < product:
                max = product
    return max            

if __name__ == '__main__':
    largest_product([[1,2], [2,3], [3,4], [1, 2, 1, 3]])