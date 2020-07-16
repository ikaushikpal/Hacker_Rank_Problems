def strangeCounter(t):
    value = 3
    while t > value:
        t = t-value
        value *= 2
    print(value-t+1)


if __name__ == '__main__':
    t = int(input())
    strangeCounter(t)
