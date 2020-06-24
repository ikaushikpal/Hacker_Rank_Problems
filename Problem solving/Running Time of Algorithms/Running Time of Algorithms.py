def runningTime(arr):
    count = 0
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = key

    return count


print(runningTime([2, 1, 3, 1, 2]))
