def toys(w):
    w.sort()
    j, count, c, i = 0, 0, 0, 0
    while i < len(w):
        j = i+1
        c = 0
        while j < len(w):
            if w[j] - w[i] > 4:
                c += 1
                break
            j += 1
        if c > 0:
            count += 1
        i = j

    return count


toys([7, 8, 12, 15, 19, 24])
toys([1, 2, 3, 21, 7, 12, 14, 21])
toys([1, 2, 3, 4, 5, 10, 11, 12, 13])
toys([88, 34, 99, 23, 30, 84, 56, 37, 5, 55])
