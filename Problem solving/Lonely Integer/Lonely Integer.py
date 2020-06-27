def lonelyinteger(a):
    count = 0
    for value in a:
        count ^= value
    print(count)


lonelyinteger([0, 0, 1, 2, 1])
