def fairRations(B):
    count = 0
    for i in range(len(B)-1):
        if B[i] % 2 != 0:
            B[i] += 2
            count += 2
            B[i+1] += 1
    if B[len(B)-1] % 2 == 0:
        print(count)
    else:
        print('NO')


if __name__ == '__main__':
    N = int(input())
    B = list(map(int, input().rstrip().split()))
    fairRations(B)
