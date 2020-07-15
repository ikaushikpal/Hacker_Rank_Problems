import sys


def bubbleSort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        number_of_swaps = 0
        for j in range(0, n-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                number_of_swaps += 1
                count += 1

        if number_of_swaps == 0:
            break

    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[n-1]}")


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
bubbleSort(a)
