if __name__ == "__main__":
    n, m = map(int,input().split())
    comb =[]
    my_values = []
    for i in range(n):
        v= int('0b' + input(),2)
        my_values.append(v)
    result = []
    for i in range(1,m):
        for j in range(i+1,m):
            comb.append((i,j))
    mx = 0
    cnt = 0
    for i, j in comb:
        p = bin(int(my_values[i-1])|int(my_values[j-1])).count('1')
        if p > mx:
            mx=p
            cnt=1
        elif p == mx:
            cnt += 1
    print(mx)
    print(cnt)
