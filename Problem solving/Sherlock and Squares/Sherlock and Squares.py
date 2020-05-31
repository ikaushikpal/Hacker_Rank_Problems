import math

q = int(input())


for q_itr in range(q):
    a, b = map(int,input().split()) 

    print(math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1)))

