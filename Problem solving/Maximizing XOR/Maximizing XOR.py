def maximizingXor(l, r):
    count = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            if i ^ j > count:
                count = i ^ j

    print(count)


maximizingXor(11, 100)
