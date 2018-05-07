def merge_sort(list):
    if len(alist) > 1:
        import pdb; pdb.set_trace()
        middle = len(alist) // 2
        lo_half = list[:mid]
        hi_half = list[mid:]

        merge_sort(lo_half)
        merge_sort(hi_half)

        i = 0
        j = 0
        k = 0
        while i < len(lo_half) and j < len(hi_half):
            if lo_half[i] < hi_half[j]:
                alist[k] = lo_half[i]
                i += 1
            else:
                list[k] = hi_half[j]
                j += 1
            k += 1

        while i < len(lo_half):
            list[k] = lo_half[i]
            i += 1
            k += 1

        while j < len(hi_half):
            list[k] = hi_half[j]
            j += 1
            k += 1





