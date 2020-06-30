def chessboardGame(x, y):
    x = x % 4
    y = y % 4
    if((y == 0) or (y == 3) or (x == 0) or (x == 3)):
        return "First"
    else:
        return "Second"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        result = chessboardGame(x, y)
        print(result)
