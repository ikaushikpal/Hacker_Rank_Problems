def twoArrays(k, A, B):
    count = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(0, len(A)):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'


print(twoArrays(1, [0, 1], [0, 2]))
