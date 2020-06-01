n = int(input())
for _ in range(n):
    b, w = map(int,input().split())
    bc, wc, z = map(int,input().split())
    count = 0


    if bc+z <= wc:
        count = (b + w)*bc + w*z

    elif wc+z <= bc:
        count = b*z + (b + w)*wc
    else:
        count = (b*bc)+(w*wc)
    
    print(count)