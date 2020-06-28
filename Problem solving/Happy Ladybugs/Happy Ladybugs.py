def happyLadybugs(n, b):
    hasEmpty = b.count('_') > 0
    for x in b:
        if x != '_' and b.count(x) == 1:
            return "NO"
    if hasEmpty:
        return "YES"
    for i in range(0, n):
        if (i == 0 and b[i] != b[i+1]) or (i == n-1 and b[i] != b[i-1]) or (b[i] != b[i-1] and b[i] != b[i+1]):
            return "NO"
    return "YES"


if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        n = int(input())
        b = input()
        result = happyLadybugs(n, b)
        print(result)
