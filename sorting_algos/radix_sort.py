def radix_sort(my_list):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split my_list between lists
        for i in my_list:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into my_list array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                my_list[a] = i
                a += 1

        # move to next digit
        placement *= RADIX
    return my_list
