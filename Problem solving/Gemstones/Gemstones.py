def gemstones(arr):
    Hash = ['']*len(arr)
    min_length = 2**16
    for i in range(len(Hash)):
        string = list(set(arr[i]))
        string.sort()
        Hash[i] = string
        if len(string) < min_length:
            min_length = len(string)
    count = 0

    for i in range(min_length):
        flag = 0
        key = Hash[0][i]
        for j in range(1, len(Hash)):
            if key != Hash[j][i]:
                flag = 1
        # if flag == 0:
        #     count += 1
        # else:
        #     break

    print(count)


gemstones(['basdfj',
           'asdlkjfdjsa',
           'bnafvfnsd',
           'oafhdlasd', ])
