def maximumPerimeterTriangle(sticks):
    triangles = dict()
    for i in range(len(sticks)):
        for j in range(i+1, len(sticks)):
            for k in range(j+1, len(sticks)):
                a, b, c = sticks[i], sticks[j], sticks[k]
                if (a + b <= c) or (a + c <= b) or (b + c <= a):
                    continue
                else:
                    perimeter = a + b + c
                    triangles[perimeter] = [a, b, c]

    if len(triangles.keys()):
        result = triangles[max(triangles.keys())]
        result.sort()
        print(*result)
    else:
        print(-1)


if __name__ == '__main__':
    n = int(input())
    sticks = list(map(int, input().rstrip().split()))
    maximumPerimeterTriangle(sticks)
