def countSort(arr):
    maxx = max(arr)
    Hash = [0]*(maxx+1)
    for value in arr:
        Hash[value] += 1
    i, j = 0, 0
    while i <= maxx:
        if Hash[i] > 0:
            arr[j] = i
            Hash[i] -= 1
            j += 1
        else:
            i += 1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    countSort(arr)
    print(*arr)