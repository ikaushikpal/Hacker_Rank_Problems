def stone(n, a, b):
    solutions = set()
    for i in range(n):
        solutions.add(a * i + b * (n-i-1))
 
    return solutions
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = int(input())
        b = int(input())
        l = sorted(list(stone(n, a, b)))
        for value in l:
            print(value,end=' ')
        print()