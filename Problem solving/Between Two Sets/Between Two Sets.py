def getTotalX(a, b):
    start = a[len(a)-1]
    end = b[0]
    tot = a + b
    count = 0
    for i in range(start, end+1):
        flag = 0
        for v in tot:
            if v > i:
                if v % i != 0:
                    flag = 1
                    break
            else:
                if i % v != 0:
                    flag = 1
                    break
        if flag == 0:
            count += 1
    print(count)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    getTotalX(arr, brr)
