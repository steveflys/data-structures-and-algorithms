"""Write a function that accepts an array of positive integers, and returns an array sorted by a radix sort algorithm."""


def radix_sort(my_list):
    """Define a radix sort."""
    if len(my_list) < 2:
        return my_list
        
    RADIX = 10
    maxLength = False
    tmp = -1
    placement = 1

    while not maxLength:
        maxLength = True
        """declare and initialize buckets"""
        buckets = [list() for _ in range(RADIX)]

        """split my_list between lists"""
        for i in my_list:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        """empty lists into my_list array"""
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                my_list[a] = i
                a += 1

        """move to next digit"""
        placement *= RADIX
    return my_list
