def birthdayCakeCandles(arr):
    arr.sort()
    count = 1
    for i in range(len(arr)-2,0,-1):
        if arr[len(arr)-1]==arr[i]:
            count += 1
    print(count)


# print(birthdayCakeCandles([3 ,2, 1 ,3]))
li = [3 ,2, 1 ,3]
print(li.count(3))