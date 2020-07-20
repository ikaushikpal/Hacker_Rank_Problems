from math import sqrt, ceil


def primeOrNot(n):
    end = ceil(sqrt(n))+2
    if(n == 1):
        print("Not prime")
        return
    if(n == 2):
        print("Prime")
        return
    for i in range(2, end):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")


t = int(input())
for i in range(t):
    n = int(input())
    primeOrNot(n)
