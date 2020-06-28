def countingSort(arr):
    Hash = [0]*(100)
    for value in arr:
        Hash[value] += 1
    for v in Hash:
        print(v,end=' ')


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    countingSort(arr)