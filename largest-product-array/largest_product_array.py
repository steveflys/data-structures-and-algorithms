def largest_product(list):
    
    def largest_product(list):
        product = 0
        index = 0
        for x in list:
            step = list[index[0]] * list[index[1]]
            if step > product:
                product = step
            step = list[index[0]] * list[index + 1[0]]
            if step > product:
                product = step
            step = list[index[1]] * list[index + 1[1]]     
            if step > product:
                product = step
            index += 1
        return product      

if __name__ == '__main__':
    largest_product