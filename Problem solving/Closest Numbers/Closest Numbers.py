from collections import deque


def closestNumbers(arr):
    arr.sort()
    q = deque([arr[0]])
    i = 1
    result = dict()
    while i < len(arr):
        q.append(arr[i])
        value = abs(arr[i]-arr[i-1])
        if value in result:
            result[value].append([arr[i-1], arr[i]])
        else:
            result[value] = [[arr[i-1], arr[i]]]
        q.popleft()
        i += 1

    min_value = min(result.keys())
    for List in result[min_value]:
        print(*List, end=' ')


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    closestNumbers(arr)
