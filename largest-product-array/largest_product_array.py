
def largest_product(list_in):
    product = 0
    index = 0
    max_index = -1
    for x in list_in:
        max_index += 1

    for x in list_in:
        step_1 = list_in[index][0] * list_in[index][1]
        if step_1 > product:
            product = step_1
        if index == max_index:
            return product
        step_2 = list_in[index][0] * list_in[index + 1][0]
        if step_2 > product:
            product = step_2
        step_3 = list_in[index][1] * list_in[index + 1][1]
        if step_3 > product:
            product = step_3
        index += 1
    return product
