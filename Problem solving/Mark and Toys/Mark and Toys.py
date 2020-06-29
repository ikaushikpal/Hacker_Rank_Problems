def maximumToys(prices, k):
    prices.sort()
    sum = 0
    for i in range(len(prices)):
        if sum > k:
            print(i-1)
            return
        sum += prices[i]
    print(len(prices)-1)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    maximumToys(prices, k)
